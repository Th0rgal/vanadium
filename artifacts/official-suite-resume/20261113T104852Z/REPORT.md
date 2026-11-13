# Official Bitcoin full suites — parent assessment

Status: IN_PROGRESS_WITH_FAILURES. Raw evidence independently inspected through checkpoint 15. No global PASS.

| Complete fresh run | Passed | Failed | Skipped/ignored | Deselected/filtered | Exit |
|---|---:|---:|---:|---:|---:|
| Native CTest: 30 upstream + added Lean target, SPECULOS=ON | 31 | 0 | 0 | 0 | 0 |
| Entire official tests_mainnet directory, NanoS+, slow=2 | 2 | 0 | 0 | 0 | 0 |
| Entire official tests_mainnet directory, NanoX, slow=2 | 2 | 0 | 0 | 0 | 0 |
| Separate Bitcoin Rust app workspace | 90 | 0 | 0 | 0 | 0 |
| Separate Bitcoin Rust common workspace | 81 unit + 4 integration | 0 | 0 | 0 | 0 |
| Root Vanadium common, PRIVATE minimal lock overlay | 66 | 0 | 0 | 0 | 0 |
| Entire official testnet tests directory, NanoS+, slow=2, timeout=300 | 279 | 2 | 1 | 0 | 1 |
| Entire official testnet tests directory, NanoX, slow=2, timeout=300 | 279 | 2 | 1 | 0 | 1 |

Both testnet runs collected and executed 282 cases. Exact argv, terminal summaries, completed exit records, and JUnit independently agree. No collection errors or selection filters. These complete runs failed; they are not passing certification. Counts are per attempt, never summed across retries.

CTest counts executable targets, not individual CMocka cases. Full LastTest.log has 31 passed target markers, zero failed markers, and names matching JUnit. CMake cache sets SPECULOS=ON and native C compiler=/usr/bin/cc; installed LLVM21 is separate tooling provenance. Mainnet uses official legacy fixtures. Bitcoin common integrations are BIP352:1, BIP374:2, BIP375:1; doc tests:0. Historical app79/90, common74/81 and device subset counts remain unverified.

## Observed failures and pending validation

1. `test_sign_psbt_singlesig_wpkh_512to256`: both full runs hit `Failed: Timeout >300.0s` during host Python fixture construction in txmaker/key.py, before client.sign_psbt. Separate exact-case diagnostics with timeout=1800 also exit1 on both devices, now inside select.select waiting for APDU during signing. Those narrow diagnostics do not certify the full suite or establish a device bug.
2. `test_sign_psbt_musig2_evicts_oldest_session`: both full runs report requests.ConnectionError, connection refused at Speculos API ports5001/5101. Why Speculos disappears is not yet established. An isolated exact NanoX diagnostic passes1 with exit0 in69.85s; this is not full-suite acceptance or proof of the original cause.

The single upstream skip is `test_get_extended_pubkey_non_standard_reject_early`, instructions.py:105. Nano devices can reject only at the last step; the early-rejection test does not apply. Upstream skip rules are unchanged. No added exclusions or weakened assertions.

Continue diagnosis of one failure at a time, followed by complete same-selection validation with a measured runtime budget. Narrow diagnostics and longer time limits do not imply success. Original overlapped0x6901 failure remains preserved; the case passes in the fresh isolated full run, but its original cause is unproven.

Root Vanadium common is distinct from Bitcoin common. Its original exact --locked canary exits101 before execution: the existing workspace lock lacks cargo-vnd→rhai_codegen dependency metadata. Original Cargo.lock SHA256 remains139326fa0b3bd5d75ba9447549493fd135330d1f2bf51a0d9c95ee50a04e7546. The authorized PRIVATE nightly --lockfile-path overlay adds exactly the missing edge to the already locked rhai_codegen3.1.0 package, no other changes. Parent independently verified actual lock bytes/TOML/diff and the full66pass/doc0,0fail/ignored/filtered,exit0. Private overlaySHA c5b183fda05b625d50581e943e52f280c9ca46ee13a590e0252c8034789785d6; original frozen --locked failure remains unchanged and separately labelled.

## Pins and operational evidence

Vanadium source6ee1f9545e2efaed439d463a02187c73a9d6d1b4, public contract ref045439a8c1a984b67f13b913df7c75002ef732a7. Appafe126fea70c8c7d6091948bb8a8ae529ea89a60. Lean baselinef68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb, emitter8c3503fa0df74fafcd7a3b91e4319606985b7198. Emitter executableSHA256e0fdcc83ac1273c077da6be968e8a4287851ba7756173e53c5a85a669c21cc98. Authentic FFI archivee01676d36e77e8fa22368f7331f498a7af2bd7a0276b95a2968c7e66c069f889:45exports,0undefined,maxhostframe296bytes. CandidateA092bb97 was never substituted.

SDKv27.1.7 SHA9ea0fae9b40bb91e7c4f94bb0e9b8cf22df36306. Fresh12:17:16Z provenance confirms pins and empty tracked source diffs. New nested Bitcoin lockfiles are archived as actual files, patch and independently matched hashes; generated untracked tests/tests paths still need inventory.

All four original monitored runs completed before12:20Z. The monitor logs all completed at12:17:23Z and exits on that condition before its deadline branch. No monitor replacement or PID-absence claim. The superseded monitor-only Codex helper was cancelled, native health confirmed, with no observed actions. New diagnostics remain executor-owned; do not reuse the obsolete12:20 cutoff. Boat expiry is14:22:27Z following a budget-checked120minute extension, incremental commitment$0.144. Last daily budget observation:$36.04/$50.

Every prior interrupted, failed or prerequisite attempt remains distinct. Initial Docker/SDK/Python/emitter errors were resolved through authentic public native provisioning without rights changes or stubs. Large checkpoint13 raw logs use reproducible gzip; delta-manifest.json provides original paths, byte counts and SHA256. Full uncompressed snapshots remain in parent artifacts.

Only new owned trees and private Boat output are writable. No shared/site/RAM edits, source/spec changes, extra reviewers, merge or deployment. Progress is signed and pushed to public Th0rgal/vanadium evidence branch after LedgerHQ403, with remote SHA verification.

Checkpoint14: both identical-selection full282 slow2 reruns with timeout1800 are active, currently512case; no finalcounts/exit. New monitorPID625880 active deadline14:20Z,started12:21:02Z,signals[] independently observed; Boat14:22:27Z. Fullarchive transfer failed twice with transport_unavailable; SHA-verified individualfiles secured instead, splitimmutablearchive requested. Currentjob4.16GiB cgroup haszeroOOM events, not proof ofhistoricalcause. No spec changes.

Checkpoint15: no new completed result; full1800 reruns still512case at12:41:41. Both APIs respond200 with Loading transaction (read-only12:38 snapshot); no inference of forwardprogress or eventualpass. Exact original-lock canary also exits101 on same nightlyCargo as acceptedprivateoverlay. Requested splitmanifest missing (harvest_not_found); individualproofs secured and splittransfer request reiterated.

Checkpoint16: executor healthy active; live owned Boat expiry14:22:27Z, budget36.04/50USD. Independently SHA-verified runtime and screen snapshots12:43 show live pytest/Core/Speculos/QEMU and both APIs200 Loading transaction. No completed result or forward APDU progress established. No timeout escalation justified from this snapshot. Split manifest remains harvest_not_found; no atomic snapshot claimed. Prior accepted results and complete full300 failures unchanged. No source/spec changes.

Checkpoint17: healthy active executor; Boat expiry14:22:27Z, budget36.04/50USD. Fresh full1800 stdout both remain512case37%, no finalcounts/exit. Same-PID snapshots12:43:20 to12:48:15 show each Speculos Python about285userCPU seconds, each QEMU about1.8userCPU seconds. This identifies CPU activity chiefly host Speculos Python, not forwardAPDUprogress or genuinebug. Executor informed to diagnose before blind timeout escalation. Splitmanifest stillharvest_not_found; SHAverified individualfiles retained. Prior completed suites/failures unchanged, no source/spec changes.

Checkpoint18: executor healthy active; Boat ready expiry14:22:27Z, dailybudget36.04/50USD. Full1800 attempts are INCOMPLETE_PROCESS_LOSS, not running or certified: raw process-loss observation13:01:39 reports monitor625880, runners626268/626269,pytest626271/626272 and all Core/Speculos absent. Cause UNKNOWN, no completion records; both exact completion JSON harvest_not_found. Raw stdout both contains512to256 FAILED marker38%, continues toMuSig eviction61% then ends without traceback/summary; stderr empty. Last monitor12:57:17 shows no completions, actual deadline14:20Z. No inference of OOM, TTL kill, emulator bug or finalcounts. Secured individualfiles/receipts SHAverified, no atomicarchiveclaim. Splitmanifest stillmissing. Request diagnosis of process lifetime/cgroup/system evidence and safe durable runner before restart; do not repeat passing suites or blindtimeout escalation. All previously accepted complete results and complete full300 failures retained unchanged. No source/spec changes.

Checkpoint19: executor healthy active, Boat14:22:27Z, budget36.04/50USD. New full1800 retry3 launch receipts13:07:12 use pristine baseline app, entire directory slow2/no filters, fresh Core datadirs/RPC25443/26443. Fresh stdout collected282 and ends at4toMax_go_back36%; no finalcounts/exit accepted. Worker reports retry2 interrupted due stale Core datadir permanent error; original processloss remains UNKNOWN. New monitor receiptPID945842 deadline14:20; loaded receipt alone not independent proof of continued process lifetime.

Confirmed separate fixture bug: setup_node retries permanent Core JSONRPC errors forever. Minimal two-line else:raise patch inspected on pristine afe126f; three focused regressions before2pass1fail (retried permanent error), after3pass, stdout/exitJSON/JUnit independently match. Transient ConnectionError and Loading wallet retries preserved. Parent applied exact patch in owned local app tree, diffcheck/AST passed, signed public branch test/official-node-setup-permanent-error-20261113 remoteSHA702ca8c41b35bf9f6b018a28d569965a37329281 verified. No Lean contract change warranted for fixture behavior. Official suites still baseline; regression is separate from official acceptance.

Generated tests/tests inventory acquired with exact paths/sizes/SHA: private Core regtest chain/wallet/config outputs, no code stubs observed. Splitmanifest exactpath stillharvest_not_found; live-checkpoint.py only creates hugearchive, actual split implementation explicitly requested. Individual files SHAverified; no atomicarchiveclaim. Prior complete suites/failures retained. No additional reviewers or spec/assertion/skip changes.
