//! Freestanding Lean Miniscript validation bridge (`VND-BUG-006`).
//!
//! Encodes BIP-388 [`DescriptorTemplate`] Miniscript AST nodes into the compact
//! postfix byte stream specified by `SPEC_ABI.md` (`llb_miniscript_check_postfix`)
//! and validates type correctness (`B/V/K/W`, `z/o/n/d/u`), BIP-379 non-malleability
//! (`m`), signature presence (`s`), height/time timelock conflict freedom (`k`),
//! and BIP-68 `older(n)` / BIP-65 `after(n)` consensus ranges with zero heap
//! allocation.

use crate::account::{DescriptorTemplate, TapTree, WalletPolicy};
use crate::errors::Error;

const OP_ZERO: u8 = 0x00;
const OP_ONE: u8 = 0x01;
const OP_PK_K: u8 = 0x02;
const OP_PK_H: u8 = 0x03;
const OP_PK: u8 = 0x04;
const OP_PKH: u8 = 0x05;
const OP_OLDER: u8 = 0x06;
const OP_AFTER: u8 = 0x07;
const OP_SHA256: u8 = 0x08;
const OP_HASH256: u8 = 0x09;
const OP_RIPEMD160: u8 = 0x0A;
const OP_HASH160: u8 = 0x0B;
const OP_MULTI: u8 = 0x0C;
const OP_MULTI_A: u8 = 0x0D;

const OP_WRAP_A: u8 = 0x10;
const OP_WRAP_S: u8 = 0x11;
const OP_WRAP_C: u8 = 0x12;
const OP_WRAP_T: u8 = 0x13;
const OP_WRAP_D: u8 = 0x14;
const OP_WRAP_V: u8 = 0x15;
const OP_WRAP_J: u8 = 0x16;
const OP_WRAP_N: u8 = 0x17;
const OP_WRAP_L: u8 = 0x18;
const OP_WRAP_U: u8 = 0x19;

const OP_AND_V: u8 = 0x20;
const OP_AND_B: u8 = 0x21;
const OP_AND_N: u8 = 0x22;
const OP_OR_B: u8 = 0x23;
const OP_OR_C: u8 = 0x24;
const OP_OR_D: u8 = 0x25;
const OP_OR_I: u8 = 0x26;
const OP_ANDOR: u8 = 0x27;
const OP_THRESH: u8 = 0x28;

/// Require non-malleability (`bit 0`: `top.m`) and at least one signature (`bit 1`: `top.s`),
/// in addition to `top.base == B` and `top.k` (no height/time timelock mix).
pub const REQUIRE_SANE_TOPLEVEL: u8 = 0x03;

struct PostfixBuf {
    bytes: [u8; llb_vanadium_ffi::MINISCRIPT_MAX_POSTFIX_OPS],
    len: usize,
}

impl PostfixBuf {
    #[inline]
    const fn new() -> Self {
        Self {
            bytes: [0u8; llb_vanadium_ffi::MINISCRIPT_MAX_POSTFIX_OPS],
            len: 0,
        }
    }

    #[inline]
    fn push_u8(&mut self, b: u8) -> Result<(), Error> {
        if self.len >= self.bytes.len() {
            return Err(Error::InvalidWalletPolicy);
        }
        self.bytes[self.len] = b;
        self.len += 1;
        Ok(())
    }

    #[inline]
    fn push_u16_le(&mut self, v: u16) -> Result<(), Error> {
        let le = v.to_le_bytes();
        self.push_u8(le[0])?;
        self.push_u8(le[1])
    }

    #[inline]
    fn push_u32_le(&mut self, v: u32) -> Result<(), Error> {
        let le = v.to_le_bytes();
        self.push_u8(le[0])?;
        self.push_u8(le[1])?;
        self.push_u8(le[2])?;
        self.push_u8(le[3])
    }

    #[inline]
    fn as_slice(&self) -> &[u8] {
        &self.bytes[..self.len]
    }
}

fn encode_miniscript_postfix(desc: &DescriptorTemplate, out: &mut PostfixBuf) -> Result<(), Error> {
    match desc {
        DescriptorTemplate::Zero => out.push_u8(OP_ZERO),
        DescriptorTemplate::One => out.push_u8(OP_ONE),
        DescriptorTemplate::Pk_k(_) => out.push_u8(OP_PK_K),
        DescriptorTemplate::Pk_h(_) => out.push_u8(OP_PK_H),
        DescriptorTemplate::Pk(_) => out.push_u8(OP_PK),
        DescriptorTemplate::Pkh(_) => out.push_u8(OP_PKH),
        DescriptorTemplate::Older(n) => {
            out.push_u8(OP_OLDER)?;
            out.push_u32_le(*n)
        }
        DescriptorTemplate::After(n) => {
            out.push_u8(OP_AFTER)?;
            out.push_u32_le(*n)
        }
        DescriptorTemplate::Sha256(_) => out.push_u8(OP_SHA256),
        DescriptorTemplate::Hash256(_) => out.push_u8(OP_HASH256),
        DescriptorTemplate::Ripemd160(_) => out.push_u8(OP_RIPEMD160),
        DescriptorTemplate::Hash160(_) => out.push_u8(OP_HASH160),
        DescriptorTemplate::Multi(k, kps) | DescriptorTemplate::Sortedmulti(k, kps) => {
            let k_u16 = u16::try_from(*k).map_err(|_| Error::InvalidMultisigQuorum)?;
            let n_u16 = u16::try_from(kps.len()).map_err(|_| Error::TooManyKeys)?;
            out.push_u8(OP_MULTI)?;
            out.push_u16_le(k_u16)?;
            out.push_u16_le(n_u16)
        }
        DescriptorTemplate::Multi_a(k, kps) | DescriptorTemplate::Sortedmulti_a(k, kps) => {
            let k_u16 = u16::try_from(*k).map_err(|_| Error::InvalidMultisigQuorum)?;
            let n_u16 = u16::try_from(kps.len()).map_err(|_| Error::TooManyKeys)?;
            out.push_u8(OP_MULTI_A)?;
            out.push_u16_le(k_u16)?;
            out.push_u16_le(n_u16)
        }
        DescriptorTemplate::A(x) => {
            encode_miniscript_postfix(x, out)?;
            out.push_u8(OP_WRAP_A)
        }
        DescriptorTemplate::S(x) => {
            encode_miniscript_postfix(x, out)?;
            out.push_u8(OP_WRAP_S)
        }
        DescriptorTemplate::C(x) => {
            encode_miniscript_postfix(x, out)?;
            out.push_u8(OP_WRAP_C)
        }
        DescriptorTemplate::T(x) => {
            encode_miniscript_postfix(x, out)?;
            out.push_u8(OP_WRAP_T)
        }
        DescriptorTemplate::D(x) => {
            encode_miniscript_postfix(x, out)?;
            out.push_u8(OP_WRAP_D)
        }
        DescriptorTemplate::V(x) => {
            encode_miniscript_postfix(x, out)?;
            out.push_u8(OP_WRAP_V)
        }
        DescriptorTemplate::J(x) => {
            encode_miniscript_postfix(x, out)?;
            out.push_u8(OP_WRAP_J)
        }
        DescriptorTemplate::N(x) => {
            encode_miniscript_postfix(x, out)?;
            out.push_u8(OP_WRAP_N)
        }
        DescriptorTemplate::L(x) => {
            encode_miniscript_postfix(x, out)?;
            out.push_u8(OP_WRAP_L)
        }
        DescriptorTemplate::U(x) => {
            encode_miniscript_postfix(x, out)?;
            out.push_u8(OP_WRAP_U)
        }
        DescriptorTemplate::And_v(x, y) => {
            encode_miniscript_postfix(x, out)?;
            encode_miniscript_postfix(y, out)?;
            out.push_u8(OP_AND_V)
        }
        DescriptorTemplate::And_b(x, y) => {
            encode_miniscript_postfix(x, out)?;
            encode_miniscript_postfix(y, out)?;
            out.push_u8(OP_AND_B)
        }
        DescriptorTemplate::And_n(x, y) => {
            encode_miniscript_postfix(x, out)?;
            encode_miniscript_postfix(y, out)?;
            out.push_u8(OP_AND_N)
        }
        DescriptorTemplate::Or_b(x, z) => {
            encode_miniscript_postfix(x, out)?;
            encode_miniscript_postfix(z, out)?;
            out.push_u8(OP_OR_B)
        }
        DescriptorTemplate::Or_c(x, z) => {
            encode_miniscript_postfix(x, out)?;
            encode_miniscript_postfix(z, out)?;
            out.push_u8(OP_OR_C)
        }
        DescriptorTemplate::Or_d(x, z) => {
            encode_miniscript_postfix(x, out)?;
            encode_miniscript_postfix(z, out)?;
            out.push_u8(OP_OR_D)
        }
        DescriptorTemplate::Or_i(x, z) => {
            encode_miniscript_postfix(x, out)?;
            encode_miniscript_postfix(z, out)?;
            out.push_u8(OP_OR_I)
        }
        DescriptorTemplate::Andor(x, y, z) => {
            encode_miniscript_postfix(x, out)?;
            encode_miniscript_postfix(y, out)?;
            encode_miniscript_postfix(z, out)?;
            out.push_u8(OP_ANDOR)
        }
        DescriptorTemplate::Thresh(k, subs) => {
            let k_u16 = u16::try_from(*k).map_err(|_| Error::InvalidWalletPolicy)?;
            let n_u16 = u16::try_from(subs.len()).map_err(|_| Error::InvalidWalletPolicy)?;
            for sub in subs {
                encode_miniscript_postfix(sub, out)?;
            }
            out.push_u8(OP_THRESH)?;
            out.push_u16_le(k_u16)?;
            out.push_u16_le(n_u16)
        }
        // Descriptor wrappers (`sh`, `wsh`, `wpkh`, `tr`) are never valid inside Miniscript.
        DescriptorTemplate::Sh(_)
        | DescriptorTemplate::Wsh(_)
        | DescriptorTemplate::Wpkh(_)
        | DescriptorTemplate::Tr(_, _) => Err(Error::InvalidScriptContext),
    }
}

/// Validates a Miniscript AST fragment in either P2WSH (`is_tapscript == false`) or
/// BIP-342 Tapscript (`is_tapscript == true`) context using the freestanding Lean
/// `llb_miniscript_check_postfix` kernel.
pub fn check_miniscript_expr(
    desc: &DescriptorTemplate,
    is_tapscript: bool,
    require_flags: u8,
) -> Result<(), Error> {
    let mut postfix = PostfixBuf::new();
    encode_miniscript_postfix(desc, &mut postfix)?;
    let require_non_malleable = (require_flags & 0x01) != 0;
    let require_sig = (require_flags & 0x02) != 0;
    if llb_vanadium_ffi::miniscript_check_postfix(
        postfix.as_slice(),
        is_tapscript,
        require_non_malleable,
        require_sig,
    ) {
        Ok(())
    } else {
        Err(Error::InvalidWalletPolicy)
    }
}

/// Validates every Tapscript leaf in a [`TapTree`] under BIP-379 / BIP-388 sanity rules.
pub fn check_taptree_miniscript(tree: &TapTree) -> Result<(), Error> {
    match tree {
        TapTree::Script(leaf) => check_miniscript_expr(leaf, true, REQUIRE_SANE_TOPLEVEL),
        TapTree::Branch(l, r) => {
            check_taptree_miniscript(l)?;
            check_taptree_miniscript(r)
        }
    }
}

/// Validates a full BIP-388 [`DescriptorTemplate`] against Ledger hardware wallet
/// script-context and Miniscript sanity rules (`VND-BUG-006`).
pub fn check_descriptor_template(desc: &DescriptorTemplate) -> Result<(), Error> {
    match desc {
        DescriptorTemplate::Pkh(_) | DescriptorTemplate::Wpkh(_) => Ok(()),
        DescriptorTemplate::Sh(inner) => match inner.as_ref() {
            DescriptorTemplate::Wpkh(_) => Ok(()),
            DescriptorTemplate::Multi(k, kps) | DescriptorTemplate::Sortedmulti(k, kps) => {
                if kps.len() > 20 {
                    return Err(Error::TooManyKeys);
                }
                if *k == 0 || (*k as usize) > kps.len() {
                    return Err(Error::InvalidMultisigQuorum);
                }
                Ok(())
            }
            DescriptorTemplate::Wsh(wsh_inner) => {
                check_miniscript_expr(wsh_inner, false, REQUIRE_SANE_TOPLEVEL)
            }
            _ => Err(Error::InvalidScriptContext),
        },
        DescriptorTemplate::Wsh(wsh_inner) => {
            check_miniscript_expr(wsh_inner, false, REQUIRE_SANE_TOPLEVEL)
        }
        DescriptorTemplate::Tr(_, None) => Ok(()),
        DescriptorTemplate::Tr(_, Some(tree)) => check_taptree_miniscript(tree),
        _ => Err(Error::InvalidScriptContext),
    }
}

/// Validates a [`WalletPolicy`]'s descriptor template using [`check_descriptor_template`].
#[inline]
pub fn check_wallet_policy_miniscript(policy: &WalletPolicy) -> Result<(), Error> {
    check_descriptor_template(policy.descriptor_template())
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::account::KeyInformation;
    use crate::script::ToScript;
    use alloc::vec;
    use alloc::vec::Vec;

    const XPUB0: &str = "[f5acc2fd/48'/1'/0'/2']tpubDFAqEGNyad35aBCKUAXbQGDjdVhNueno5ZZVEn3sQbW5ci457gLR7HyTmHBg93oourBssgUxuWz1jX5uhc1qaqFo9VsybY1J5FuedLfm4dK";
    const XPUB1: &str = "[d5365b22/48'/1'/0'/2']tpubDFWK5mCX28dt6hfy74Bc51jjbWrimXow1bTxCMpJrWqesK3AeZiYn8tcLFW3VoBiHhM9FjKdLWaC3GZVVX5PfGNG3zfbM14bMb1SLym36nN";

    fn keys(n: usize) -> Vec<KeyInformation> {
        let all = [XPUB0, XPUB1];
        all[..n]
            .iter()
            .map(|s| KeyInformation::try_from(*s).unwrap())
            .collect()
    }

    #[test]
    fn bug_006_accepts_sane_wsh_and_tapscript_policies() {
        let p_andor =
            WalletPolicy::new("wsh(andor(pk(@0/**),older(100),pk(@1/**)))", keys(2)).unwrap();
        assert!(check_wallet_policy_miniscript(&p_andor).is_ok());
        assert!(p_andor.to_script(false, 0).is_ok());

        let p_tr = WalletPolicy::new(
            "tr(@0/<0;1>/*,and_v(v:pk(@1/<0;1>/*),older(52596)))",
            keys(2),
        )
        .unwrap();
        assert!(check_wallet_policy_miniscript(&p_tr).is_ok());
        assert!(p_tr.to_script(false, 0).is_ok());
    }

    #[test]
    fn bug_006_rejects_older_zero_and_disable_flag() {
        assert!(!llb_vanadium_ffi::miniscript_older_ok(0));
        assert!(!llb_vanadium_ffi::miniscript_older_ok(0x8000_0001));
        assert!(!llb_vanadium_ffi::miniscript_older_ok(0x0001_0001));
        assert!(llb_vanadium_ffi::miniscript_older_ok(1));
        assert!(llb_vanadium_ffi::miniscript_older_ok(0x0040_0001));

        if let Ok(p_zero) = WalletPolicy::new("wsh(and_v(v:pk(@0/**),older(0)))", keys(1)) {
            assert_eq!(
                check_wallet_policy_miniscript(&p_zero),
                Err(Error::InvalidWalletPolicy)
            );
            assert!(p_zero.to_script(false, 0).is_err());
        }

        if let Ok(p_disable) =
            WalletPolicy::new("wsh(and_v(v:pk(@0/**),older(2147483649)))", keys(1))
        {
            assert_eq!(
                check_wallet_policy_miniscript(&p_disable),
                Err(Error::InvalidWalletPolicy)
            );
            assert!(p_disable.to_script(false, 0).is_err());
        }
    }

    #[test]
    fn bug_006_rejects_after_zero_and_msb_set() {
        assert!(!llb_vanadium_ffi::miniscript_after_ok(0));
        assert!(!llb_vanadium_ffi::miniscript_after_ok(0x8000_0000));
        assert!(llb_vanadium_ffi::miniscript_after_ok(1));
        assert!(llb_vanadium_ffi::miniscript_after_ok(500_000_000));

        if let Ok(p_zero) = WalletPolicy::new("wsh(and_v(v:pk(@0/**),after(0)))", keys(1)) {
            assert_eq!(
                check_wallet_policy_miniscript(&p_zero),
                Err(Error::InvalidWalletPolicy)
            );
            assert!(p_zero.to_script(false, 0).is_err());
        }
    }

    #[test]
    fn bug_006_rejects_timelock_height_time_mixing() {
        // Mixing block-height `after(100)` (< 500_000_000) and MTP `after(500000000)` in `and_v`
        // makes the conjunction permanently unsatisfiable / consensus-conflicting (`k == false`).
        if let Ok(p_mix_after) = WalletPolicy::new(
            "wsh(and_v(v:pk(@0/**),and_v(v:after(100),after(500000000))))",
            keys(1),
        ) {
            assert_eq!(
                check_wallet_policy_miniscript(&p_mix_after),
                Err(Error::InvalidWalletPolicy)
            );
            assert!(p_mix_after.to_script(false, 0).is_err());
        }

        // Mixing block-relative `older(1)` and time-relative `older(4194305)` (`1 | (1 << 22)`).
        if let Ok(p_mix_older) = WalletPolicy::new(
            "wsh(and_v(v:pk(@0/**),and_v(v:older(1),older(4194305))))",
            keys(1),
        ) {
            assert_eq!(
                check_wallet_policy_miniscript(&p_mix_older),
                Err(Error::InvalidWalletPolicy)
            );
            assert!(p_mix_older.to_script(false, 0).is_err());
        }
    }

    #[test]
    fn bug_006_rejects_missing_signature_and_malleable_scripts() {
        // `older(100)` alone has `s == false` (anyone can spend without a signature once aged).
        if let Ok(p_nosig) = WalletPolicy::new("wsh(older(100))", vec![]) {
            assert_eq!(
                check_wallet_policy_miniscript(&p_nosig),
                Err(Error::InvalidWalletPolicy)
            );
        }

        // `or_b(pk(@0/**),s:older(100))` has `s == false` on the aging branch (`top.s == false`).
        if let Ok(p_or_nosig) =
            WalletPolicy::new("wsh(or_b(pk(@0/**),s:older(100)))", keys(1))
        {
            assert_eq!(
                check_wallet_policy_miniscript(&p_or_nosig),
                Err(Error::InvalidWalletPolicy)
            );
            assert!(p_or_nosig.to_script(false, 0).is_err());
        }

        // `d:` in P2WSH lacks `u` (unconditional unit), making `or_i(d:v:pk(@0/**),pk(@1/**))` invalid/malleable;
        // also test raw postfix `d:v:1` malleability rejection directly.
        let mut ops = PostfixBuf::new();
        ops.push_u8(OP_ONE).unwrap();
        ops.push_u8(OP_WRAP_V).unwrap();
        ops.push_u8(OP_WRAP_D).unwrap();
        assert!(!llb_vanadium_ffi::miniscript_check_postfix(
            ops.as_slice(),
            false,
            true,
            true
        ));

        // Top-level `K` (`pk_k` without `c:`) is rejected because `top.base != B`.
        let mut pk_k_ops = PostfixBuf::new();
        pk_k_ops.push_u8(OP_PK_K).unwrap();
        assert!(!llb_vanadium_ffi::miniscript_check_postfix(
            pk_k_ops.as_slice(),
            false,
            true,
            true
        ));
    }
}
