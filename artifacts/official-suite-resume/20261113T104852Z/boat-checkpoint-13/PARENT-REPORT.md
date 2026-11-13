# Checkpoint13 — complete testnet FAIL on both devices

Independently matched exact pytest argv,282collected,282JUnit cases, terminal summaries and exit1: NanoS+279pass/2fail/1skip/0error/0deselected; NanoX identical. Full official directory, slow2, timeout300, no selection filters. Durations1699.90s/1698.33s. Complete execution is accepted; no passing certification or globalPASS.

Failure1:512to256 Timeout>300s in hostPython txmaker/key.py fixture preparation before client.sign_psbt. Separate narrow1800diagnostics also fail on bothdevices, now inside select.select waiting forAPDU during client.sign_psbt. This establishes runtime phases, not a device correctness bug or eventual success. Failure2:MuSig oldest-session eviction yields requests.ConnectionError/connectionrefused SpeculosAPI5001/5101; rootcause unproven. New isolated diagnostic-eviction-nanox active; no diagnosticPASS.

Single upstreamskip: test_get_extended_pubkey_non_standard_reject_early, instructions.py105. Nano devices permit rejection only atlaststep, so earlyrejection does not apply. No exclusions or assertions altered.

All4 originalwatchedruns completed before12:20; monitorlog12:17:23 allcompleted and codebreak beforedeadline branch. No forced cutoff affected these complete results. No claim of scriptdeadline change or processPIDabsence. Superseded monitor-only Codex helper cancelled, healthconfirmed; no observed actions. New diagnostics remain executor-owned; Boat14:22:27Z and oldcutoff must not be reused.

Fresh provenance12:17:16Z source/SDK/Lean/emitter pins match, tracked diffs empty, rootlockhash unchanged. Pinned emitter executableSHA256 e0fdcc83ac1273c077da6be968e8a4287851ba7756173e53c5a85a669c21cc98 verified. Rootcommon private minimaloverlay and generated untracked tests/tests inventory still pending. Original root --locked101 distinct from Bitcoincommon81+4. No specchanges justified.

Large rawdelta logs are reproducibly gzip compressed; delta-manifest.json stores exact uncompressedSHA256 and paths. Originals retained in full parent snapshot.
