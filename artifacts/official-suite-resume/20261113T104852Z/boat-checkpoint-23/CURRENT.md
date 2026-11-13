# COMPLETED_WITH_FAILURES — all requested suites executed; device acceptance fails.

Current completed result summary (each row is a separate suite):

|Suite|Pass|Fail|Skip|Errors|Deselected|Exit|Complete|
|---|---:|---:|---:|---:|---:|---:|---|
|ctest_full|31|0|0|0|0|0|True|
|mainnet_nanosp|2|0|0|0|0|0|True|
|mainnet_nanox|2|0|0|0|0|0|True|
|testnet_nanosp|280|1|1|0|0|1|True|
|testnet_nanox|280|1|1|0|0|1|True|
|bitcoin_rust_app|90|0|0|0|0|0|True|
|bitcoin_rust_common|85|0|0|0|0|0|True|
|root_common_overlay_full|66|0|0|0|0|0|True|


Full Ragger tests/ ran unchanged on both nanosp and nanox:282 collected, slow=2, timeout1800, no exclusions, each280passed/1failed/1upstream skip/0errors/0deselected, exit1. Terminal summaries and JUnit agree. Elapsed nanosp3002.39s and nanox3035.75s. Both MuSig2 session-eviction cases PASSED in these full runs. Only test_sign_psbt_singlesig_wpkh_512to256 failed, at1674.649s/1716.747s: requests.ConnectionError/RemoteDisconnected during Speculos ticker single-step navigation. These failures occurred BEFORE1800s and are NOT pytest timeout failures. The screen snapshots showed Loading transaction. Raw logs retain APDU traffic and full setup/call output; emulator exit status was not separately retained by upstream fixture, and no fatal diagnostic establishes the connection loss cause. This is completed failing acceptance evidence, not a missing prerequisite or a demonstrated Bitcoin behavior bug. Safe next step: serial exact-case reproduction retaining Speculos/QEMU exit and HTTP server diagnostics. No assertion/skip/spec change is justified.

Full mainnet directory completed2passed/0failed/0skip/0errors/0deselected on each device, slow2, distinct mainnet binaries. Full native CTest completed31passed/0failed/0skipped at TARGET level only, upstream30+1added, SpeculosON. Full cmocka LastTest.log and CMakeCache included; native CMake C compiler is /usr/bin/cc with SPECULOS=ON, separate from LLVM21 app/FFI tooling. Passing CTest was not repeated. Configure attempts below are per-run. Separate locked Bitcoin Rust app90passed, common85passed(81unit+4integration). Root common66passed with authorized private minimal lock overlay; original locked canary remains local source/lock inconsistency exit101, not a Bitcoin bug. Overlay canary1passed/65filtered first. No original tracked lock changed.

Pinned turbo-lean baseline8c3503fa0df74fafcd7a3b91e4319606985b7198 was explicitly checked out and rebuilt with jobs1/6144MiB bound. Rebuilt executable SHA256e0fdcc83ac1273c077da6be968e8a4287851ba7756173e53c5a85a669c21cc98 emitted authentic f68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb host FFI:45exports/0undefined/maxhoststack296bytes. CandidateA never substituted. Earlier15676ea emitter build/rejection remains historical. Host archive SHA256e01676d36e77e8fa22368f7331f498a7af2bd7a0276b95a2968c7e66c069f889.

Vanadium remote+HEAD045439a8c1a984b67f13b913df7c75002ef732a7, app remote+HEADafe126fea70c8c7d6091948bb8a8ae529ea89a60. SDK9ea0fae9b40bb91e7c4f94bb0e9b8cf22df36306, builder98693c3b63446779677d35bd7ed7c5923949ab01, native CTest Speculosad72692eacd8d961a42c95d5c4fda9d3573c2427. Fresh source/SDK/Speculos status, tracked diffs and compiler/tool versions in final-provenance-1359.*. Baseline tracked diffs empty. Core32.1 upstream release verification, public authentic native prerequisites and build records retained. Mainnet/testnet builds distinct DEBUG=0; no autoapprove. Generated tests/tests Core outputs were inventoried, not source substitutes.

Original root Cargo.lock SHA256139326fa0b3bd5d75ba9447549493fd135330d1f2bf51a0d9c95ee50a04e7546 unchanged. Private overlay SHA256c5b183fda05b625d50581e943e52f280c9ca46ee13a590e0252c8034789785d6 adds only cargo-vnd->rhai_codegen edge, no package/version/checksum changes. New nested app/common locks and patches archived; original tracked locks preserved byte-for-byte. Return core-setup-permanent-error.patch, nested-lockfiles.patch and root-common-overlay.patch for parent signing/review; no commits/signing/push performed.

Earlier full300 device runs each279passed/2failed/1skip, exit1, remain distinct: host PSBT generation Timeout300 and eviction connection-refused. Narrow1800 diagnostics failed by timeout, not full-suite certification. First1800 sessions disappeared without receipts; counts/exits null. Retry2 stale Core datadir setup loop was interrupted explicitly; fresh retry3 full runs above completed. All history/raw logs retained. Earlier ragger-tests-nanosp-long/nanox-long attempts were explicitly interrupted after about60s for the then-assumed TTL and have exit2; they are incomplete and superseded, not acceptance results. No later full1800 run was interrupted for that superseded TTL. The final retry3 runs both completed normally with exit1 before the extended expiry.

Parent extended expiry to14:22:27Z; executor did not rent/extend. Active final monitor PID945842 loaded14:20Z, sent no signals, and exited13:58:11Z after both completion receipts. Earlier monitor/process losses and explicit interruptions separately recorded. No privilege/Docker bypass, credentials, source/spec weakening, added exclusions, golden regeneration, other models/reviewers/subagents, merge/deploy or push. Heavy work only this Boat, jobs<=4/Rust1. Regression mocks isolate fixture retry behavior only; no mocked official acceptance. Initial preparation and some interactive read-only probes were not individually archived; outputs/exits were never invented.


Separate fixture implementation: core-setup-permanent-error.patch propagates permanent Core JSONRPC errors immediately; no change to transient startup retries. Regression original1failed/2passed, fixed3passed. Implemented only in new app-fixture-fix clone; current baseline official runs remain unchanged. This fixes a confirmed fixture bug, not an established Bitcoin behavioral defect. Patch applies cleanly to pristine pinned app source. See fixture-fix-notes.md and before/after exact logs; regression counts are separate from official acceptance.


At13:06Z retry2 was interrupted with SIGINT because both reused stale interrupted Core datadirs. Exact RPC probe returned database already exists(-4) for test_wallet; unchanged setup_node catches and retries this non-loading JSONRPC error indefinitely. Core stopped normally via bitcoin-cli. Fresh retry3 full-directory slow2/1800 runs started with never-existing datadirs and new RPC/P2P ports25443/25444 and26443/26444; tests/source unchanged. Prior retry2 exits/partial counts retained, not suite results. Monitor-retry3-active.json records current14:20Z cutoff and PID.


Historical mainnet-nanox first attempt:1failure/1error, exit1; GET_VERSION returned0x6901, then dashboard HTTP connection closed. It overlapped earlier testnet execution on default Speculos ports. After stopping the overlapping testnet pytest and using dedicated mainnet binaries, mainnet-nanox2 completed2/0/0. Default-port session overlap was observed, but the cause of the original0x6901 remains UNPROVEN; later isolated passes do not establish its cause. Historical ragger-tests-nanosp2:282collected,9passed/1failed, KeyboardInterrupt exit2; first failure bolt3_received_htlc returned0x6901. The exit2 interruption and overlap history remain recorded; it was not completed as a suite, and no cause is inferred from a later pass. Later isolated full300 runs pass that node; no source fix or regression claim is justified for this unreproduced failure.

Emitter chronology: initial emitter-public-build/rejection used15676ea244a08d386f8047c4bbfe0416692d1089 and is historical, not baseline acceptance. pin-compatible-emitter explicitly checked out8c3503fa0df74fafcd7a3b91e4319606985b7198 (exit0), then compatible-emitter-build rebuilt lean-native with one worker and6144MiB bound (exit0), before successful baseline emission. Exact hashes and fresh checkout/status are in provenance-1304.*.

At13:01Z previous1800 pytest runners and monitor were absent without completion records (last monitor12:57:17Z). Cause unknown; no executor signal. Counts/exits remain null. Fresh unchanged full-directory1800 retry2 runs launched13:02Z; see process-loss-1301.json and individual launch receipts. Monitor restart uses14:20Z cutoff.

```json
{
  "ctest_full": {
    "exit": 0,
    "pass": 31,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 31,
    "execution_complete": true,
    "log": "ctest-full"
  },
  "fixture_regression_before": {
    "exit": 1,
    "pass": 2,
    "fail": 1,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 3,
    "terminal_summary": "========================= 1 failed, 2 passed in 0.06s ==========================",
    "execution_complete": true,
    "suite_complete": false,
    "log": "fixture-regression-before-final"
  },
  "fixture_regression_after": {
    "exit": 0,
    "pass": 3,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 3,
    "terminal_summary": "============================== 3 passed in 0.01s ===============================",
    "execution_complete": true,
    "suite_complete": false,
    "log": "fixture-regression-after-final"
  },
  "historical_mainnet_nanox_failed": {
    "exit": 1,
    "pass": 0,
    "fail": 1,
    "skip": 0,
    "errors": 1,
    "deselected": 0,
    "reported_cases": 2,
    "terminal_summary": "========================== 1 failed, 1 error in 0.18s ==========================",
    "execution_complete": true,
    "suite_complete": true,
    "log": "mainnet-nanox"
  },
  "historical_nanosp2_aborted": {
    "exit": 2,
    "pass": 9,
    "fail": 1,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 11,
    "terminal_summary": "============= 1 failed, 9 passed, 13 warnings in 66.20s (0:01:06) ==============",
    "execution_complete": false,
    "suite_complete": false,
    "log": "ragger-tests-nanosp2"
  },
  "mainnet_nanosp": {
    "exit": 0,
    "pass": 2,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 2,
    "terminal_summary": "============================== 2 passed in 2.41s ===============================",
    "execution_complete": true,
    "suite_complete": true,
    "log": "mainnet-nanosp"
  },
  "mainnet_nanox": {
    "exit": 0,
    "pass": 2,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 2,
    "terminal_summary": "============================== 2 passed in 2.36s ===============================",
    "execution_complete": true,
    "suite_complete": true,
    "log": "mainnet-nanox2"
  },
  "testnet_nanosp": {
    "exit": 1,
    "pass": 280,
    "fail": 1,
    "skip": 1,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 282,
    "terminal_summary": "===== 1 failed, 280 passed, 1 skipped, 274 warnings in 3002.39s (0:50:02) ======",
    "execution_complete": true,
    "suite_complete": true,
    "log": "ragger-tests-nanosp-1800-full-retry3"
  },
  "testnet_nanox": {
    "exit": 1,
    "pass": 280,
    "fail": 1,
    "skip": 1,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 282,
    "terminal_summary": "===== 1 failed, 280 passed, 1 skipped, 274 warnings in 3035.75s (0:50:35) ======",
    "execution_complete": true,
    "suite_complete": true,
    "log": "ragger-tests-nanox-1800-full-retry3"
  },
  "stale_datadir_nanosp": {
    "exit": 2,
    "pass": 1,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 1,
    "terminal_summary": "================== 1 passed, 3 warnings in 287.82s (0:04:47) ===================",
    "execution_complete": false,
    "suite_complete": false,
    "log": "ragger-tests-nanosp-1800-full-retry2"
  },
  "stale_datadir_nanox": {
    "exit": 2,
    "pass": 1,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 1,
    "terminal_summary": "================== 1 passed, 3 warnings in 287.83s (0:04:47) ===================",
    "execution_complete": false,
    "suite_complete": false,
    "log": "ragger-tests-nanox-1800-full-retry2"
  },
  "interrupted_1800_nanosp": {
    "status": "NO_COMPLETION_RECORD",
    "pass": null,
    "fail": null,
    "skip": null,
    "errors": null,
    "deselected": null,
    "exit": null,
    "log": "ragger-tests-nanosp-1800-full"
  },
  "interrupted_1800_nanox": {
    "status": "NO_COMPLETION_RECORD",
    "pass": null,
    "fail": null,
    "skip": null,
    "errors": null,
    "deselected": null,
    "exit": null,
    "log": "ragger-tests-nanox-1800-full"
  },
  "testnet_nanosp_300": {
    "exit": 1,
    "pass": 279,
    "fail": 2,
    "skip": 1,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 282,
    "terminal_summary": "===== 2 failed, 279 passed, 1 skipped, 273 warnings in 1699.90s (0:28:19) ======",
    "execution_complete": true,
    "suite_complete": true,
    "log": "ragger-tests-nanosp-final2"
  },
  "testnet_nanox_300": {
    "exit": 1,
    "pass": 279,
    "fail": 2,
    "skip": 1,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 282,
    "terminal_summary": "===== 2 failed, 279 passed, 1 skipped, 273 warnings in 1698.33s (0:28:18) ======",
    "execution_complete": true,
    "suite_complete": true,
    "log": "ragger-tests-nanox-final"
  },
  "initial_testnet_nanosp": {
    "status": "NO_COMPLETION_RECORD",
    "pass": null,
    "fail": null,
    "skip": null,
    "errors": null,
    "deselected": null,
    "exit": null,
    "log": "ragger-tests-nanosp3"
  },
  "initial_testnet_nanox": {
    "status": "NO_COMPLETION_RECORD",
    "pass": null,
    "fail": null,
    "skip": null,
    "errors": null,
    "deselected": null,
    "exit": null,
    "log": "ragger-tests-nanox"
  },
  "bitcoin_rust_app": {
    "exit": 0,
    "pass": 90,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "rust_result_groups": [
      [
        90,
        0,
        0,
        0,
        0
      ]
    ],
    "execution_complete": true,
    "log": "bitcoin-app-with-ffi"
  },
  "bitcoin_rust_common": {
    "exit": 0,
    "pass": 85,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "rust_result_groups": [
      [
        81,
        0,
        0,
        0,
        0
      ],
      [
        1,
        0,
        0,
        0,
        0
      ],
      [
        2,
        0,
        0,
        0,
        0
      ],
      [
        1,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        0
      ]
    ],
    "execution_complete": true,
    "log": "bitcoin-common-with-ffi"
  },
  "root_common_canary": {
    "exit": 101,
    "pass": null,
    "fail": null,
    "skip": null,
    "errors": null,
    "deselected": null,
    "execution_complete": false,
    "log": "common-canary"
  },
  "root_common_overlay_canary": {
    "exit": 0,
    "pass": 1,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 65,
    "rust_result_groups": [
      [
        1,
        0,
        0,
        0,
        65
      ]
    ],
    "execution_complete": true,
    "log": "root-common-overlay-canary"
  },
  "root_common_overlay_full": {
    "exit": 0,
    "pass": 66,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "rust_result_groups": [
      [
        66,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        0
      ]
    ],
    "execution_complete": true,
    "log": "root-common-overlay-full"
  },
  "testnet_nanosp_long": {
    "exit": 2,
    "pass": 1,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 1,
    "terminal_summary": "=================== 1 passed, 3 warnings in 60.30s (0:01:00) ===================",
    "execution_complete": false,
    "suite_complete": false,
    "log": "ragger-tests-nanosp-long"
  },
  "testnet_nanox_long": {
    "exit": 2,
    "pass": 4,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 5,
    "terminal_summary": "======================== 4 passed, 7 warnings in 59.21s ========================",
    "execution_complete": false,
    "suite_complete": false,
    "log": "ragger-tests-nanox-long"
  },
  "diagnostic_512_nanosp": {
    "status": "NO_COMPLETION_RECORD",
    "pass": null,
    "fail": null,
    "skip": null,
    "errors": null,
    "deselected": null,
    "exit": null,
    "log": "diagnostic-512-nanosp"
  },
  "diagnostic_512_nanox": {
    "status": "NO_COMPLETION_RECORD",
    "pass": null,
    "fail": null,
    "skip": null,
    "errors": null,
    "deselected": null,
    "exit": null,
    "log": "diagnostic-512-nanox"
  },
  "testnet_nanosp_final": {
    "exit": 1,
    "pass": 279,
    "fail": 2,
    "skip": 1,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 282,
    "terminal_summary": "===== 2 failed, 279 passed, 1 skipped, 273 warnings in 1699.90s (0:28:19) ======",
    "execution_complete": true,
    "suite_complete": true,
    "log": "ragger-tests-nanosp-final2"
  },
  "testnet_nanox_final": {
    "exit": 1,
    "pass": 279,
    "fail": 2,
    "skip": 1,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 282,
    "terminal_summary": "===== 2 failed, 279 passed, 1 skipped, 273 warnings in 1698.33s (0:28:18) ======",
    "execution_complete": true,
    "suite_complete": true,
    "log": "ragger-tests-nanox-final"
  },
  "diagnostic_512_nanosp_retry": {
    "exit": 1,
    "pass": 0,
    "fail": 1,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 1,
    "terminal_summary": "================== 1 failed, 2 warnings in 1801.20s (0:30:01) ==================",
    "execution_complete": true,
    "suite_complete": false,
    "log": "diagnostic-512-nanosp-retry"
  },
  "diagnostic_512_nanox_retry": {
    "exit": 1,
    "pass": 0,
    "fail": 1,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 1,
    "terminal_summary": "================== 1 failed, 2 warnings in 1801.02s (0:30:01) ==================",
    "execution_complete": true,
    "suite_complete": false,
    "log": "diagnostic-512-nanox-retry"
  },
  "diagnostic_eviction_nanox": {
    "exit": 0,
    "pass": 1,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 1,
    "terminal_summary": "=================== 1 passed, 2 warnings in 69.85s (0:01:09) ===================",
    "execution_complete": true,
    "suite_complete": false,
    "log": "diagnostic-eviction-nanox"
  }
}
```

## Configure attempts (per-run, not aggregated)

app-configure: exit 1; see exact argv and logs.

ctest-native-configure: exit 0; see exact argv and logs.

ctest-llvm21-configure: exit 0; see exact argv and logs.

