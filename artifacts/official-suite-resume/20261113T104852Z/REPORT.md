# Official Bitcoin suite resume — current parent assessment

Status: IN_PROGRESS. Evidence reviewed through checkpoint6. No global PASS.

| Complete fresh suite | Passed | Failed | Skipped/ignored | Deselected/filtered | Exit |
|---|---:|---:|---:|---:|---:|
| Native CTest, all31targets (30upstream+added Lean target), SpeculosON |31|0|0|0|0|
| Official mainnet directory, NanoS+, slow2 |2|0|0|0|0|
| Official mainnet directory, NanoX, slow2 |2|0|0|0|0|
| Bitcoin Rust app, separate workspace |90|0|0|0|0|
| Bitcoin Rust common, separate workspace |81unit+4integration|0|0|0|0|

Mainnet uses the official legacy fixture suite, distinct from testnet Ragger. Rust common integrations are BIP3521,BIP3742,BIP3751; doc0. CTest counts executable targets, not individual cmocka cases; full LastTest.log requested, JUnit stdout truncates at1024bytes. Parent independently matched exact argv, completed exits and raw summaries/JUnit. See counts.json and checkpoint parent-inspection files. Historical app79/90/common74/81/subsetdevice counts remain unverified, never reused as fresh evidence.

## Incomplete suites and observed failures

Full testnet Ragger NanoS+/NanoX both collected282 with slow2 and isolated emulator/BitcoinCore ports. Complete counts remain unknown while running. An earlier overlapping attempt stopped after9pass/1fail RAPDU0x6901; it is retained and not certified. Isolated runs reportedly passed that early case but full raw completion is still required before resolving cause. Enabled512-input case hits300-second runner limit on bothdevices; separate longer diagnostics and queued full timeout1800 runs preserve assertions/selection/skips. None of these partial/diagnostic outputs is PASS.

Root Vanadium common is a DIFFERENT crate from Bitcoincommon81: original --locked canary exits101 before compilation because workspace lock lacks cargo-vnd->rhai_codegen edge. Upstream lock remains byte-identical SHA256139326fa0b3bd5d75ba9447549493fd135330d1f2bf51a0d9c95ee50a04e7546. A private --lockfile-path overlay investigation is authorized, with exact diff/lock recorded and any result clearly distinguished from frozen original. No upstream lock rewrite or silent --locked removal.

## Reproduction pins and provenance

Vanadium source6ee1f9545e2efaed439d463a02187c73a9d6d1b4, public evidence/contract ref045439a8c1a984b67f13b913df7c75002ef732a7. Appafe126fea70c8c7d6091948bb8a8ae529ea89a60. Leanf68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb. Correct emitter8c3503fa0df74fafcd7a3b91e4319606985b7198 rebuilt on dedicatedBoat; candidateA092bb97 not substituted. Authentic host FFIarchivee01676d36e77e8fa22368f7331f498a7af2bd7a0276b95a2968c7e66c069f889, undefined0, maximumhostframe296bytes. SDKv27.1.7 SHA9ea0fae9b40bb91e7c4f94bb0e9b8cf22df36306, compiler21, native user-space dependencies. New private nested Rust locks archived as patch/hashes.

Initial failures (Dockerdenied,CMakeSDKmissing,Pythondependencies,staleemitter) are preserved as individual raw records; public native provisioning resolved them without socket/group changes or stubs. They are not Bitcoin bugs. Original phase1 report/counts preserved as initial-PHASE1 files. Worker REPORT.md inside older archives remains stale; current parent assessment supersedes it.

Only NEW owned integration/test trees used; no shared/site/RAM edits. No specs/tests/assertions weakened or changed, no added exclusions or reviewers, no merge/deploy. Exact commands/stdout/stderr/exits in checkpoint records; remote evidence branchtest/official-resume-evidence-20261113 signed and pushed to publicTh0rgal/vanadium after LedgerHQ403. Machine/executor IDs,TTL12:22Z and ownership in state.json.
