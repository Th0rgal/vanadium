# IN_PROGRESS — authorized extension, current evidence

Parent extended this owned Boat expiry to1794579747 (2026-11-13T14:22:27Z). No executor rental/extension. Old monitor already exited after prior tests completed; no pytest/Core/Speculos signals were sent during repair. Replacement monitor (latest PID in monitor-retry3-active.json) wrote its loaded14:20Z deadline to monitor-extension-active.json and runtime-monitor-extension.stdout; process existence independently confirmed. Prior11:50 start limit superseded.

Fresh FULL Ragger tests/ runs started perdevice nanosp/nanox, same282 collection, slow=2, timeout1800, unchanged skip rules/assertions/selection. New API5501/5601 and real Core32.1 RPC23443/24443, unique datadirs, authentic testnet binaries unchanged. Read per-run launch/active/completed JSON; incomplete counts null. Runner sessions keep exact commands and write exits only on observed completion; process loss never supplies an inferred exit.

Prior full timeout300 results are COMPLETED:279passed/2failed/1upstream skip/0errors/0deselected perdevice, exit1,282collected. Failures:512-input host PSBT generation timeout and Speculos connection refusal during musig2 session eviction. Exact512 timeout1800 diagnostics also failed both devices waiting in Ragger APDU select; neither is full-suite evidence. Narrow eviction nanox retry passed1/1 in69.85s; does not override failed full runs. These findings require new FULL1800 results, not subset certification.

Completed unchanged results: CTest31/0/0 target level (upstream30+1added), native SpeculosON; Bitcoin Rust app90passed and common85passed (81unit+4integration), both locked; full mainnet2passed perdevice, slow2, distinct mainnet binaries. No CTest rerun. native-ctest/Testing/Temporary/LastTest.log is full62,480-byte CMocka output; native-ctest/CMakeCache.txt included. Configure attempts listed per run below.

Original root-common exact locked canary exits101 before compilation due LOCAL manifest/lock inconsistency (cargo-vnd/rhai_codegen edge), not Bitcoin behavior or external SDK absence. Parent authorized a private minimal --lockfile-path overlay. Exact canary passed1 with65filtered; FULL common then passed66/0/0/0, exit0 (0doctests). Original tracked Cargo.lock remains unchanged. Overlay adds only cargo-vnd->rhai_codegen; no version/checksum/package changes. Overlay SHA256c5b183fda05b625d50581e943e52f280c9ca46ee13a590e0252c8034789785d6, original/overlay/patch and exact commands archived. Authentic installed Cargo1.87nightly supplies unstable lockfile-path option; rustc/rustdoc1.100stable compile the tests; no bootstrap or source changes. Original failure evidence remains separate. Comparison with the same nightly Cargo but original lock and --locked also exits101 before compilation, confirming the overlay is required rather than attributing success to Cargo version alone. Root lock SHA256139326fa0b3bd5d75ba9447549493fd135330d1f2bf51a0d9c95ee50a04e7546.

Authentic baseline Lean f68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb FFI generated using public turbo-lean8c3503fa0df74fafcd7a3b91e4319606985b7198. Executable SHA256e0fdcc83ac1273c077da6be968e8a4287851ba7756173e53c5a85a669c21cc98; baseline/CandidateA never swapped. Host archive45exports/0undefined/296-byte max host stack. Newly generated nested Bitcoin locks and nested-lockfiles.patch retained for parent signing. Existing tracked locks unchanged.

Source pins: vanadium045439a8c1a984b67f13b913df7c75002ef732a7; app-bitcoinafe126fea70c8c7d6091948bb8a8ae529ea89a60; SDKv27.1.7 9ea0fae9b40bb91e7c4f94bb0e9b8cf22df36306; builder98693c3b63446779677d35bd7ed7c5923949ab01; native Speculos ad72692eacd8d961a42c95d5c4fda9d3573c2427. Versions/status/full tracked diffs in final-provenance-frozen.*; tracked diffs empty. Private untracked tests/tests outputs were inventoried with sizes/hashes: Core regtest wallets/journals/chainstate/config and fee estimator outputs, no code stubs. Inventory in extension-provenance-followups.stdout. Authentic LLVM21.1.8, Core32.1 upstream-verified, CMocka1.1.7, Python Speculos0.27.4/Ragger1.47.4, ARM tools privately provisioned.

No assertions/spec/source weakening, stubs, golden regeneration, added exclusions, credentials, privileges, Docker bypass, push/merge/deploy, reviewers/models/subagents. Build jobs<=4, Rust1, heavy work only this VM. Historical reports/attempts explicitly retained. Original root blocker is local source/lock inconsistency, not a Bitcoin bug; no overall PASS claim. Every completed test/build run has exact argv/cwd/private env, stdout/stderr and exit. Initial preparation and some interactive read-only probes were not individually archived; no output fabricated.

## Per-run results


Separate fixture implementation: core-setup-permanent-error.patch propagates permanent Core JSONRPC errors immediately; no change to transient startup retries. Regression original1failed/2passed, fixed3passed. Implemented only in new app-fixture-fix clone; current baseline official runs remain unchanged. This fixes a confirmed fixture bug, not an established Bitcoin behavioral defect. Patch applies cleanly to pristine pinned app source. See fixture-fix-notes.md and before/after exact logs; regression counts are separate from official acceptance.


At13:06Z retry2 was interrupted with SIGINT because both reused stale interrupted Core datadirs. Exact RPC probe returned database already exists(-4) for test_wallet; unchanged setup_node catches and retries this non-loading JSONRPC error indefinitely. Core stopped normally via bitcoin-cli. Fresh retry3 full-directory slow2/1800 runs started with never-existing datadirs and new RPC/P2P ports25443/25444 and26443/26444; tests/source unchanged. Prior retry2 exits/partial counts retained, not suite results. Monitor-retry3-active.json records current14:20Z cutoff and PID.


Historical mainnet-nanox first attempt:1failure/1error, exit1; GET_VERSION returned0x6901, then dashboard HTTP connection closed. It overlapped earlier testnet execution on default Speculos ports. After stopping the overlapping testnet pytest and using dedicated mainnet binaries, mainnet-nanox2 completed2/0/0. Port/session interference is supported by overlap and remediation, but0x6901 alone is not proof of a Bitcoin defect. Historical ragger-tests-nanosp2:282collected,9passed/1failed, KeyboardInterrupt exit2; first failure bolt3_received_htlc returned0x6901. It was interrupted to stop overlapping default-port execution, not completed as a suite. Later isolated full300 runs pass that node; no source fix or regression claim is justified for this unreproduced failure.

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
    "terminal_summary": "=================== 1 failed, 2 passed, 76 warnings in 0.18s ===================",
    "execution_complete": true,
    "suite_complete": false,
    "log": "fixture-regression-before"
  },
  "fixture_regression_after": {
    "exit": 0,
    "pass": 3,
    "fail": 0,
    "skip": 0,
    "errors": 0,
    "deselected": 0,
    "reported_cases": 3,
    "terminal_summary": "============================== 3 passed in 0.02s ===============================",
    "execution_complete": true,
    "suite_complete": false,
    "log": "fixture-regression-after"
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
    "status": "NO_COMPLETION_RECORD",
    "pass": null,
    "fail": null,
    "skip": null,
    "errors": null,
    "deselected": null,
    "exit": null,
    "log": "ragger-tests-nanosp-1800-full-retry3"
  },
  "testnet_nanox": {
    "status": "NO_COMPLETION_RECORD",
    "pass": null,
    "fail": null,
    "skip": null,
    "errors": null,
    "deselected": null,
    "exit": null,
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

