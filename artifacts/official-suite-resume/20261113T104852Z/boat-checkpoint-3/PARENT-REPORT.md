# Checkpoint3: official mainnet2/2 on both devices; full testnet still incomplete

Parent checked exact argv, raw stdout, exit0 and JUnit for mainnet-nanosp and mainnet-nanox2. Each invocation ran the entire tests_mainnet directory with --enable_slow_tests=2:2pass,0fail,0skip,0deselected. This is the official mainnet fixture suite, distinct from testnet Ragger. Earlier nanox attempt exit1 (1failure+1error) remains in raw evidence; successful retry not used to erase it. Exact cause/remediation requested.

CTest31/31 remains accepted from checkpoint2. Its LastTest.log and fresh source status requested; not present in this snapshot yet.

Testnet NanoS+ interrupted attempt collected282items,9pass/1fail before KeyboardInterrupt exit2. First failure test_e2e_miniscript_bolt3_received_htlc RAPDU0x6901 is executable-observed but not yet established implementation bug; no spec relaxation justified. Running/retry full testnet counts remain unknown. No full testnet PASS.

Authentic public Lean driver now builds, but recorded emitter source15676ea244a08d386f8047c4bbfe0416692d1089 differs from requested baseline8c3503fa0df74fafcd7a3b91e4319606985b7198. Parent requested explicit pinned baseline build/hash before accepting Rust results. No candidateA artifact accepted.

All attempts and initial prerequisite errors remain separate. Worker REPORT.md is still old checkpoint1; current raw logs/counts and this parent report supersede it. Sources/specs/tests not changed by parent; root Cargo.lock preserved. Boat executor active, expiry12:22Z, no additional review.
