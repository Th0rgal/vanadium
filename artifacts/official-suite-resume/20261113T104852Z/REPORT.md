# Official Bitcoin suite resume — current parent assessment

Status: IN_PROGRESS. Evidence reviewed through checkpoint12. No global PASS.

| Complete fresh suite | Passed | Failed | Skipped/ignored | Deselected/filtered | Exit |
|---|---:|---:|---:|---:|---:|
| Native CTest, all31targets (30upstream+added Lean target), SpeculosON |31|0|0|0|0|
| Official mainnet directory, NanoS+, slow2 |2|0|0|0|0|
| Official mainnet directory, NanoX, slow2 |2|0|0|0|0|
| Bitcoin Rust app, separate workspace |90|0|0|0|0|
| Bitcoin Rust common, separate workspace |81unit+4integration|0|0|0|0|

Mainnet uses the official legacy fixture suite, distinct from testnet Ragger. Rust common integrations are BIP3521,BIP3742,BIP3751; doc0. CTest counts executable targets, not individual cmocka cases; full LastTest.log now independently inspected:31 passed markers,0 failed markers, names matchJUnit. Native cache compiler=/usr/bin/cc; installed LLVM21 is separate app-tooling provenance. Parent independently matched exact argv, completed exits and raw summaries/JUnit. See counts.json and checkpoint parent-inspection files. Historical app79/90/common74/81/subsetdevice counts remain unverified, never reused as fresh evidence.

## Incomplete suites and observed failures

Full testnet Ragger NanoS+/NanoX collect282 with slow2. Complete counts remain unknown. Previous full runs/512 diagnostics vanished without completed exit/JUnit; cause unproven. Timeout1800 full attempts were explicitly interrupted after about60sec forTTL, exit2 retained. Fresh timeout300 full attempts are active; independent raw NanoS+ final2 log shows earlier bolt3_received_htlc now PASSED, but original0x6901 cause remains unproven. No diagnostic or partial run certifies full suite. Parent superseded start deadline11:50 and TTL-only cutoff: full identical-selection1800 reruns remain needed if300 budget insufficient; Boat may be extended after budget check. No assertion/skip changes.

Root Vanadium common is a DIFFERENT crate from Bitcoincommon81: original --locked canary exits101 before compilation because workspace lock lacks cargo-vnd->rhai_codegen edge. Upstream lock remains byte-identical SHA256139326fa0b3bd5d75ba9447549493fd135330d1f2bf51a0d9c95ee50a04e7546. A private --lockfile-path overlay investigation is authorized, with exact diff/lock recorded and any result clearly distinguished from frozen original. No upstream lock rewrite or silent --locked removal.

## Reproduction pins and provenance

Vanadium source6ee1f9545e2efaed439d463a02187c73a9d6d1b4, public evidence/contract ref045439a8c1a984b67f13b913df7c75002ef732a7. Appafe126fea70c8c7d6091948bb8a8ae529ea89a60. Leanf68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb. Correct emitter8c3503fa0df74fafcd7a3b91e4319606985b7198 rebuilt on dedicatedBoat; candidateA092bb97 not substituted. Authentic host FFIarchivee01676d36e77e8fa22368f7331f498a7af2bd7a0276b95a2968c7e66c069f889, undefined0, maximumhostframe296bytes. SDKv27.1.7 SHA9ea0fae9b40bb91e7c4f94bb0e9b8cf22df36306, compiler21, native user-space dependencies. New private nested Rust locks archived as actual copies and patch/hashes, independently matched. Emitter executable hash still requested.

Initial failures (Dockerdenied,CMakeSDKmissing,Pythondependencies,staleemitter) are preserved as individual raw records; public native provisioning resolved them without socket/group changes or stubs. They are not Bitcoin bugs. Original phase1 report/counts preserved as initial-PHASE1 files. Worker REPORT.md through checkpoint6 was stale; checkpoint7/8 current report now preserves interruptions explicitly. Parent assessment remains authoritative.

Only NEW owned integration/test trees used; no shared/site/RAM edits. No specs/tests/assertions weakened or changed, no added exclusions or reviewers, no merge/deploy. Exact commands/stdout/stderr/exits in checkpoint records; remote evidence branchtest/official-resume-evidence-20261113 signed and pushed to publicTh0rgal/vanadium after LedgerHQ403. Machine/executor IDs,extendedTTL14:22:27Z and ownership in state.json.

Checkpoint9 corrects partial NanoX1800 retry to terminal4passed/exit2; JUnit5 includes unfinished case. Full testnet counts remain null. Monitors still have12:20Z cutoff; parent requested updating after extension. Durable workspace probe remote placement failed verification (expected artifact harvest_not_found), so do not rely on its reported completed status.

Checkpoint11 raw full300 logs show512to256 FAILED markers on bothdevices and continued execution. Finaltraceback/counts pending, so no failurecause or whole-suite result certified. Original upstream non_standard_reject_early skip markers retained; final -ra reasons pending. Boat extended120min after budgetcheck to14:22:27Z (increment$0.144). IMPORTANT runningmonitor correction from old12:20Z cutoff still unverified; resume action accepted, not proof of application.

Checkpoint12: full runs progressing69%NanoS+/76%NanoX at12:11, still no completion. A same-model Codex implementation helper (not reviewer) owns only disjoint new parent-monitor files and exact obsolete monitor intervention, because active executor has not applied queued steering. Cutoff fix awaits raw proof; tests/source/locks remain executor-owned. LiveBoatexpiry14:22:27Z and dailybudget$33.62/$50.
