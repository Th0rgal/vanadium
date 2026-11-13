# Current official-suite execution report

Status: IN_PROGRESS. This report supersedes historical-before-checkpoint3-REPORT.md and other historical attempts. Counts below are executed results; incomplete runs remain null.

Full native CTest: 31 target-level passes, zero failures/skips; upstream 30 plus one added target. Full CMocka output is native-ctest/Testing/Temporary/LastTest.log; CMakeCache.txt is included alongside it. JUnit truncation does not establish assertion-level counts. CTest was not repeated.

Full mainnet: 2 passed on nanosp and 2 passed on nanox, slow=2. These use upstream legacy Speculos fixtures. Full locked Bitcoin Rust: app 90 passed; common 85 passed (81 unit, 4 integration). No test exclusions added.

Root common locked exact canary exits101 before compilation because the unchanged upstream root lock needs an update (cargo-vnd/rhai_codegen dependency edge). This is a local manifest/lock consistency blocker, not a Bitcoin behavior failure. Safe remediation requires parent reconciliation of that existing lock or a proven matching toolchain. Root lock SHA256 139326fa0b3bd5d75ba9447549493fd135330d1f2bf51a0d9c95ee50a04e7546 remains unchanged.

Full testnet runs collect282 per device with slow=2. First full attempts used timeout300 and show a512-input failure marker but were interrupted before final traceback/exit/JUnit. At11:44Z no prior suite/queue/diagnostic processes remained and prior session IDs were unknown; cause is not established. These incomplete attempts have null counts/exit, not a fabricated exit. Fresh timeout1800 full attempts were explicitly interrupted after about60 seconds to fit existing TTL (exit2 and partial results retained). Fresh full timeout300 attempts then started11:46Z; isolated exact512 diagnostics use1800. The first nanosp restart was interrupted after observing a leftover Core node from interrupted session setup; replacement final2 uses fresh22443/22444 ports and datadir. No exclusions/assertion/skip-rule changes. A timeout remains failure, never PASS. Read per-run execution_complete/suite_complete; interrupted observed cases do not cover the full collection. Separate interrupted exact512 diagnostics are narrow runs and never counted as full-suite acceptance. Read counts.json and per-run raw logs for actual completion and outcomes. All incomplete counts remain null. Upstream skips remain unchanged and reasons appear in raw -ra summaries.

Authentic prerequisites were provisioned privately: SDK v27.1.7, LLVM21.1.8, CMocka1.1.7, QEMU8.2.2, Core32.1 (upstream setup verification), Speculos/Ragger. Public turbo-lean branch feat/freestanding-flat-ptr-loops at8c3503fa0df74fafcd7a3b91e4319606985b7198 generated baseline f68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb host FFI (45 exports, no undefined). Earlier missing-prerequisite/emitter attempts are historical, superseded by successful provisioning. Candidate A was never substituted. Extracted private libtoolize data paths were relocated to its authentic private data directory; no tests/assertions changed.

Only new private nested Cargo.lock files were generated from unchanged manifests; copies, hashes, and nested-lockfiles.patch are included for parent signing. Tracked source diffs remain empty. No credentials, push, privileges, Docker bypass, other models, or subagents. No overall PASS claim. VM TTL remains12:22Z.

## Selected completed/incomplete runs

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
  "testnet_nanox": {
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
  }
}
```

## Configure attempts (per-run, not aggregated)

app-configure: exit 1; see exact argv and logs.

ctest-native-configure: exit 0; see exact argv and logs.

ctest-llvm21-configure: exit 0; see exact argv and logs.

