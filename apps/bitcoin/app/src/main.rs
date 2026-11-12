#![cfg_attr(feature = "target_vanadium_ledger", no_std, no_main)]

extern crate alloc;

mod bip32;
mod constants;
mod handlers;
mod identity;
mod resident_key;
mod sp_keys;

use handlers::*;

use alloc::vec::Vec;

use common::message::{Request, Response};
use sdk::{App, AppBuilder};

sdk::bootstrap!();

async fn handle_request(
    app: &mut App,
    request: &Request,
) -> Result<Response, common::errors::Error> {
    match request {
        Request::GetVersion => Ok(Response::Version {
            version: alloc::string::String::from(env!("CARGO_PKG_VERSION")),
        }),
        Request::Exit => sdk::exit(0),
        Request::GetMasterFingerprint { tree } => handle_get_master_fingerprint(app, *tree),
        Request::GetExtendedPubkey {
            tree,
            path,
            display,
            identity_index,
        } => handle_get_extended_pubkey(app, *tree, path, *display, *identity_index).await,
        Request::RegisterAccount {
            name,
            account,
            registered_identities,
            key_signatures,
            show_cleartext,
        } => {
            handle_register_account(
                app,
                name,
                account,
                registered_identities.as_deref(),
                key_signatures.as_deref(),
                *show_cleartext,
            )
            .await
        }
        Request::RegisterIdentityKey { name, pubkey } => {
            handle_register_identity_key(app, name, pubkey).await
        }
        Request::GetAddress {
            name,
            account,
            por,
            coordinates,
            display,
            identity_index,
        } => {
            handle_get_address(
                app,
                name.as_deref(),
                account,
                por,
                coordinates,
                *display,
                *identity_index,
            )
            .await
        }
        Request::SignPsbt { psbt } => handle_sign_psbt(app, psbt).await,
        Request::ExportSilentPaymentScanKey { account_index } => {
            handle_export_sp_scan_key(app, *account_index).await
        }
        Request::GetHeapStats { reset } => {
            let current = sdk::current_heap_bytes() as u32;
            let peak = if *reset {
                sdk::reset_peak_heap_bytes() as u32
            } else {
                sdk::peak_heap_bytes() as u32
            };
            Ok(Response::HeapStats {
                current_bytes: current,
                peak_bytes: peak,
            })
        }
    }
}

#[sdk::handler]
async fn process_message(app: &mut App, request: &[u8]) -> Vec<u8> {
    if llb_vanadium_ffi::check_kernel_version().is_err() {
        return minicbor::to_vec(&Response::Error {
            error: common::errors::Error::InvalidRequest,
        })
        .unwrap();
    }
    let mut decoder = minicbor::Decoder::new(request);
    let Ok(decoded_request) = decoder.decode::<Request>() else {
        return minicbor::to_vec(&Response::Error {
            error: common::errors::Error::InvalidRequest,
        })
        .unwrap();
    };
    if decoder.position() != request.len() {
        return minicbor::to_vec(&Response::Error {
            error: common::errors::Error::InvalidRequest,
        })
        .unwrap();
    }
    let response = handle_request(app, &decoded_request)
        .await
        .unwrap_or_else(|error| Response::Error { error });
    minicbor::to_vec(&response).unwrap()
}

pub fn main() {
    AppBuilder::new("Bitcoin", env!("CARGO_PKG_VERSION"), process_message)
        .description("Bitcoin is ready")
        .developer("Salvatore Ingala")
        .run();
}

#[cfg(test)]
mod lean_security_tests {
    use super::*;
    use bitcoin::opcodes::all::{OP_ELSE, OP_ENDIF, OP_NOTIF};

    #[test]
    fn lean_freestanding_kernels_and_version_verified() {
        assert_eq!(
            llb_vanadium_ffi::version_packed(),
            llb_vanadium_ffi::VERSION_PACKED_EXPECTED
        );
        assert!(llb_vanadium_ffi::kernel_self_test());
    }

    #[test]
    fn get_version_request_returns_version_without_panic() {
        let mut app = sdk::App::singleton();
        let req = minicbor::to_vec(&Request::GetVersion).unwrap();
        let resp_bytes = sdk::executor::block_on(process_message(&mut app, &req));
        let resp: Response = minicbor::decode(&resp_bytes).unwrap();
        assert_eq!(
            resp,
            Response::Version {
                version: String::from(env!("CARGO_PKG_VERSION")),
            }
        );
    }

    #[test]
    fn bug_001_andor_branch_order_matches_bip379() {
        use common::account::WalletPolicy;
        use common::script::ToScript;

        let xpub0 = "tpubDCwYjpDhUdPGP5rS3wgNg13mTrrjBuG8V9VpWbyptX6TRPbNoZVXsoVUSkCjmQ8jJycjuDKBb9eataSymXakTTaGifxR6kmVsfFehH1ZgJT";
        let xpub1 = "tpubDCwYjpDhUdPGQWG6wG6hkBJuWFZEtrn7j3xwG3i8XcQabcGC53xWZm1hSXrUPFS5UvZ3QhdPSjXWNfWmFGTioARHuG5J7XguEjgg7p8PxAm";
        let policy = WalletPolicy::new(
            "wsh(andor(pk(@0/**),older(100),pk(@1/**)))",
            vec![xpub0.try_into().unwrap(), xpub1.try_into().unwrap()],
        )
        .unwrap();

        use common::script::{ScriptContext, ToScriptWithKeyInfo};
        let witness_script = match policy.descriptor_template() {
            common::bip388::DescriptorTemplate::Wsh(inner) => inner
                .to_script(policy.key_information(), false, 0, ScriptContext::Wsh)
                .unwrap(),
            _ => panic!("expected wsh"),
        };
        let bytes = witness_script.as_bytes();
        // [pk0 (34B: 0x21 <33B>) OP_CHECKSIG] OP_NOTIF [pk1 (34B) OP_CHECKSIG] OP_ELSE [older(100)] OP_ENDIF
        assert_eq!(bytes[35], OP_NOTIF.to_u8());
        // Immediately after OP_NOTIF must be Z = pk(@1/**) (push 33 bytes = 0x21), NOT Y = older(100)!
        assert_eq!(bytes[36], 0x21);
        assert_eq!(bytes[36 + 35], OP_ELSE.to_u8());
        assert_eq!(*bytes.last().unwrap(), OP_ENDIF.to_u8());
        assert!(policy.to_script(false, 0).is_ok());
    }

    #[test]
    fn bug_005_sh_wsh_derives_p2sh_p2wsh() {
        use common::account::WalletPolicy;
        use common::script::ToScript;

        let xpub0 = "tpubDCwYjpDhUdPGP5rS3wgNg13mTrrjBuG8V9VpWbyptX6TRPbNoZVXsoVUSkCjmQ8jJycjuDKBb9eataSymXakTTaGifxR6kmVsfFehH1ZgJT";
        let policy =
            WalletPolicy::new("sh(wsh(pk(@0/**)))", vec![xpub0.try_into().unwrap()]).unwrap();
        let spk = policy.to_script(false, 0).unwrap();
        assert!(spk.is_p2sh());
        assert_eq!(spk.len(), 23);
    }

    #[test]
    fn bug_007_get_extended_pubkey_rejects_depth_256() {
        let mut app = sdk::App::singleton();
        let path = common::message::Bip32Path(vec![0; 256]);
        let res = sdk::executor::block_on(handlers::handle_get_extended_pubkey(
            &mut app,
            common::message::KeyTree::Resident,
            &path,
            false,
            None,
        ));
        assert_eq!(res, Err(common::errors::Error::DerivationPathTooLong));
    }

    #[test]
    fn bug_006_register_account_rejects_unsane_miniscript_and_accepts_sane() {
        use common::account::WalletPolicy;
        use common::script::ToScript;

        let xpub0 = "tpubDCwYjpDhUdPGP5rS3wgNg13mTrrjBuG8V9VpWbyptX6TRPbNoZVXsoVUSkCjmQ8jJycjuDKBb9eataSymXakTTaGifxR6kmVsfFehH1ZgJT";
        let xpub1 = "tpubDCwYjpDhUdPGQWG6wG6hkBJuWFZEtrn7j3xwG3i8XcQabcGC53xWZm1hSXrUPFS5UvZ3QhdPSjXWNfWmFGTioARHuG5J7XguEjgg7p8PxAm";

        // Unsane timelock mix (height + time `after` in `and_v`) must be rejected by both `to_script` and `handle_register_account`.
        let unsane_timelock = WalletPolicy::new(
            "wsh(and_v(v:after(100),and_v(v:after(500000100),pk(@0/**))))",
            vec![xpub0.try_into().unwrap()],
        )
        .unwrap();
        assert_eq!(
            unsane_timelock.to_script(false, 0),
            Err(common::errors::Error::InvalidWalletPolicy)
        );
        let mut app = sdk::App::singleton();
        let reg_res = sdk::executor::block_on(handlers::handle_register_account(
            &mut app,
            "Bad policy",
            &common::message::Account::WalletPolicy(unsane_timelock),
            None,
            None,
            false,
        ));
        assert_eq!(reg_res, Err(common::errors::Error::InvalidWalletPolicy));


        // Unsane `older(0)` must be rejected.
        let older_zero = WalletPolicy::new(
            "wsh(and_v(v:pk(@0/**),older(0)))",
            vec![xpub0.try_into().unwrap()],
        )
        .unwrap();
        assert_eq!(
            older_zero.to_script(false, 0),
            Err(common::errors::Error::InvalidWalletPolicy)
        );

        // Sane `andor` policy registers and derives cleanly.
        let sane = WalletPolicy::new(
            "wsh(andor(pk(@0/**),older(100),pk(@1/**)))",
            vec![xpub0.try_into().unwrap(), xpub1.try_into().unwrap()],
        )
        .unwrap();
        assert!(sane.to_script(false, 0).is_ok());
        let ok_res = sdk::executor::block_on(handlers::handle_register_account(
            &mut app,
            "Sane policy",
            &common::message::Account::WalletPolicy(sane),
            None,
            None,
            false,
        ));
        assert!(ok_res.is_ok());
    }

    #[test]
    fn vnd_07_get_extended_pubkey_rejects_silent_nonstandard_path() {
        let mut app = sdk::App::singleton();
        // Root identity path m/1229210958' must not be exported silently (`display == false`).
        let id_path = common::message::Bip32Path(vec![0x8000_0000 | 1229210958]);
        let res = sdk::executor::block_on(handlers::handle_get_extended_pubkey(
            &mut app,
            common::message::KeyTree::Standard,
            &id_path,
            false,
            None,
        ));
        assert_eq!(res, Err(common::errors::Error::InvalidParameter));

        // With `display == true`, identity export succeeds.
        let ok_res = sdk::executor::block_on(handlers::handle_get_extended_pubkey(
            &mut app,
            common::message::KeyTree::Standard,
            &id_path,
            true,
            None,
        ));
        assert!(ok_res.is_ok());
    }

    #[test]
    fn heap_stats_tracks_peak_and_reset() {
        let mut app = sdk::App::singleton();
        let reset_req = minicbor::to_vec(&Request::GetHeapStats { reset: true }).unwrap();
        let _ = sdk::executor::block_on(process_message(&mut app, &reset_req));

        let big = alloc::vec![0xABu8; 4096];
        core::hint::black_box(&big);
        drop(big);

        let query_req = minicbor::to_vec(&Request::GetHeapStats { reset: false }).unwrap();
        let resp_bytes = sdk::executor::block_on(process_message(&mut app, &query_req));
        let resp: Response = minicbor::decode(&resp_bytes).unwrap();
        match resp {
            Response::HeapStats { peak_bytes, .. } => assert!(peak_bytes >= 4096),
            other => panic!("unexpected response: {:?}", other),
        }
    }
}
