# Official suite resume — fresh evidence 2026-11-13

Status: BLOCKED before test execution. No official suite is certified.

Pinned source: Vanadium 6ee1f9545e2efaed439d463a02187c73a9d6d1b4; app-bitcoin afe126fea70c8c7d6091948bb8a8ae529ea89a60; Lean f68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb; candidate A 092bb97fe05e4957e3f8399c04fd2434b9a902f1.

Only new worktrees official-resume-vanadium and official-resume-app are owned. Shared source, site, RAM and candidate trees were not modified. No heavy compilation was started on this host. No reviewer launched.

## Fresh checks

See inventory.txt, canary.txt, resolution.stderr.txt, resolution.lock.diff and prerequisites.txt for exact argument vectors, output and exit status. Canary: exit 101 before compilation; upstream Cargo.lock SHA-256 preserved. Official pass/fail/skip/deselected are unknown, not zero. The diagnostic metadata run without --locked was ONLY dependency resolution in the owned worktree, then restored the original lock in a finally block. It is not test evidence. The resolver diff adds rhai_codegen to cargo-vnd; offline resolution also lacks addr2line v0.24.2. This is a build prerequisite discrepancy, not an established Bitcoin behavioral bug. No spec was changed.

## Remaining acceptance

Run Bitcoin Rust tests from their own apps/bitcoin workspace, separately from Vanadium common. Run full ctest with all 30 upstream targets and the added target, checking raw enumeration. Run complete Ragger suites tests/ and tests_mainnet/ for nanosp and nanox, with --enable_slow_tests where supported by the actual runner. Preserve all upstream skip rules and explicitly record every exclusion. Record pass/fail/skip/deselected from raw output; test collection is not a run. Historical app 79/90, common 74/81 and device subset counts are unverified and separate in counts.json.

## Safe remediation

Use a dedicated Boat VM after budget/catalog inventory, with public source and no credentials; provision authentic SDK, Speculos, CMake, pytest/Ragger and device build tooling there. Do not change socket permissions or create SDK stubs. Resolve the lock discrepancy in a separately justified, reviewed dependency step, or select the matching pinned toolchain if it demonstrably preserves the upstream lock. Do not remove --locked silently. No semantic spec relaxation is justified by these environment failures. Before cloud build, establish an anonymous public path to these exact commits; original origin points at LedgerHQ, while the local custom branch is not advertised there.

## Continuation

Local prerequisite gates remain BLOCKED. A dedicated Boat large executor is active; see state.json. Budget inventory completed before rental ($0.072/h, 90min). Public forks created after original LedgerHQ push403; both pinned source refs remotely verified. Requested/effective backend codex/codex, effective model gpt-6.1-sol. No reviewer launched. Remote test evidence has not yet been accepted.
