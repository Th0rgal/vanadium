# Official Bitcoin suites — final delivery

Full official device selections pass with the explicitly patched host runtime. This does not certify the original host runtime or the original root Cargo.lock.

| Complete suite | Passed | Failed | Upstream skip | Errors | Deselected/filtered | Exit |
|---|---:|---:|---:|---:|---:|---:|
| Testnet NanoS+, entire `.`, slow2, timeout1800 | 281 | 0 | 1 | 0 | 0 | 0 |
| Testnet NanoX, entire `.`, slow2, timeout1800 | 281 | 0 | 1 | 0 | 0 | 0 |
| Mainnet NanoS+, entire `.`, slow2 | 2 | 0 | 0 | 0 | 0 | 0 |
| Mainnet NanoX, entire `.`, slow2 | 2 | 0 | 0 | 0 | 0 | 0 |
| CTest executable targets, 30 upstream + Lean target | 31 | 0 | 0 | 0 | 0 | 0 |
| Bitcoin Rust app unit tests | 90 | 0 | 0 | 0 | 0 | 0 |
| Bitcoin Rust common: 81 unit + 4 integration | 85 | 0 | 0 | 0 | 0 | 0 |
| Vanadium root common, PRIVATE minimal lock overlay | 66 | 0 | 0 | 0 | 0 | 0 |

Parent independently reconciled exact commands, full terminal output, JUnit and exit records. Testnet collected282 cases per device; names exactly match the previous full attempt. The one unchanged upstream skip is `test_get_extended_pubkey_non_standard_reject_early`, `instructions.py:105`: Nano devices reject only at the last step. No added exclusions. Mainnet ran sequentially after both testnet runs completed, using the official legacy fixtures. CTest counts targets, not individual CMocka cases. Rust doc tests0; Bitcoin common integrations BIP352:1, BIP374:2, BIP375:1.

The final testnet durations were2093.07s/2096.69s. Immutable in-pytest provenance asserts expected module paths/hashes and baseline guestELF hashes. The selection-integrity receipt compares4846 tracked test/mainnet/golden files with zero differences. No guest, SDK, Lean specification, expected screenshot, assertion or skip was changed for these passes.

## Delivered fixes and explicit host prerequisites

App branch `test/official-navigation-interruption-20261113`, signed commit `78520b6240952f64a94a77f83ba3b7e0408bbdea`, published to https://github.com/Th0rgal/app-bitcoin and remoteSHA verified. It retains unfinished navigation state across lateE000 protocol responses, without replaying clicks, restarting snapshot indices or bypassing mandatory review. The final adapterSHA256 is02618dd652e52ee7f03c70df740fae37317450850abb2eaa08feb1139014ac03, identical to the tested runtime.

This app branch requires the external Ragger resume/backend patch and Speculos callback-lifetime patch preserved as ordinary files in `boat-checkpoint-43/prerequisites/`. They have not been published as external repository branches or silently installed into site-packages. Ragger base75a33226dc92d9af964c676a96bb99183bc38f5b/v1.47.4; Speculos Python base39e6fb1503d2de2c0bc599ffec095470f46097a3. Ragger patchSHA1090ae25b23f624865add682c60ab761000e9ff55ac221a1e15d725983c85d0c; Speculos patchSHAf85345d9a3b5f5a5dda035f1484c83b95deb904f67a8874e3b771bf6b3423c07. Combined app patch frombaselineSHAeb088c4219cf5c5abd6421498e203d46fe4f4574da8fd0a877d62fa09343fe83. The runtime restores ticker/policy in finally, preserves every snapshot comparison and bounds E000 loading-screen flushing below the guest interruption threshold; unrelated errors propagate.

Independent regression evidence: snapshot before2fail→after2pass; loading before2fail2pass→after4pass; combined navigator/host46pass; real4toMaxPlus1 narrow1pass per device. Earlier callback regressions3fail5pass→8pass and Speculos full unit15pass remain separate. The separate Core fixture permanent-RPC retry fix is signed commit702ca8c41b35bf9f6b018a28d569965a37329281 on `test/official-node-setup-permanent-error-20261113`;3regressions before2pass1fail→after3pass. It is not silently bundled into the navigation branch. No Lean contract change was warranted.

## Preserved limitations and failures

Original root `cargo test --locked` still exits101 because cargo-vnd lacks the existing rhai_codegen dependency edge in the frozen lock. Original lockSHA139326fa0b3bd5d75ba9447549493fd135330d1f2bf51a0d9c95ee50a04e7546 is unchanged. Authorized PRIVATE `--lockfile-path` overlaySHAc5b183fda05b625d50581e943e52f280c9ca46ee13a590e0252c8034789785d6 adds only that edge, without package/version/checksum drift. Its66pass is distinct from the original-lock failure. Exact commands, original/overlay locks and diff are archived.

Original full timeout300 attempts:279pass2fail1skip per device,exit1. Original full timeout1800 retry3:280pass1fail1skip per device,exit1,512RemoteDisconnected. First navigation full:280pass1fail1skip per device,exit1,4toMaxPlus1 golden mismatch. All interrupted/process-loss, wrong-import and narrow diagnostic attempts remain separately recorded; counts are never combined across attempts. Historical0x6901, early MuSig connection-refused and process-loss causes are not retrospectively asserted. GDB later captured io_event exception5/interruption timeout→app_exit255 during512 host continuation; the observer stack-read error is separately preserved.

Baseline Lean f68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb and emitter8c3503fa0df74fafcd7a3b91e4319606985b7198 were used; executableSHAe0fdcc83ac1273c077da6be968e8a4287851ba7756173e53c5a85a669c21cc98. No CandidateA substitution. Existing locks unchanged; private generated nested locks archived.

## Evidence and lifecycle

Final immutable archive `boat-checkpoint-42/final.tar.gz`:14,563,426bytes, SHA25678087260c6d0ec4284fac61a617491364e695c37e5a30480d6901b494147e858. All28parts and whole hash independently verified, tar safely extracted. Fullraw/JUnit/commands/provenance and historical attempts are retained; prior large diagnostic addenda are secured in checkpoints24/28/29/31/35. Checkpoint42 signed evidence commit49c22ea191591371a464e7d34d578f4af0d81ec4 was remotely verified before cleanup. Full checkpoint history is preserved in HISTORY.md and per-checkpoint reports.

No suite reruns after passing evidence. No extra reviewer/helper, shared/site/RAM edits, secrets, stubs or privilege bypass. Dedicated Boat cleanup receipt follows in state.json. No unqualified globalPASS.

Final cleanup: destroy_managed_machine rejected lifecycle_rejected/provider_http_error (nonretryable). Fallback stop_managed_machine succeeded; independent inventory confirms stopped. Disk retained, inventory ledger_closed=false; no deletion or ledger-closure claim. Artifacts and exact implementation were signed/pushed/remotelyverified before shutdown. Final delivery complete with the stated original-lock and external-host prerequisites.
