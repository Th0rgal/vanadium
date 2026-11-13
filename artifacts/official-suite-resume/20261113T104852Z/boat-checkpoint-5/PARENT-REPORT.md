# Checkpoint5 — full Bitcoin Rust app/common passed on pinned baseline FFI

Parent matched exact separate workspace argv, completed exit0 and every raw test summary. apps/bitcoin/app:90unitpass/0fail/0ignored/0filtered. apps/bitcoin/common:81unitpass+4integrationpass (BIP3521,BIP3742,BIP3751),0doc cases,0fail/0ignored/0filtered. Counts90vs79 and81vs74 are resolved only for these fresh pinned runs; historical counts remain unverified. The root Vanadium common crate is separate and still has lockedcanary101, never conflated with Bitcoincommon.

Correct public emitter8c3503fa0df74fafcd7a3b91e4319606985b7198 rebuilt, authentic freestanding host FFI emitted from Lean baselinef68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb. Audit artifact hash e01676d36e77e8fa22368f7331f498a7af2bd7a0276b95a2968c7e66c069f889,0undefinedsymbols,maxframe296bytes; executable hash still requested. Existing upstream root lock preserved; new private nested locks captured as patch/hashes. No candidateA substitution.

CTest31/31 and mainnet2/2 per device remain accepted. Full testnet Ragger results remain pending; previous interrupted failure0x6901 preserved, no spec relaxation. Parent instructed safe optional private Cargo --lockfile-path overlay for rootcommon, preserving upstream original and archiving exact diff; overlay success must be labeled separately from original locked failure. No silent lock change authorized.

Worker REPORT still stale, parent report and exact raw records/current counts supersede. No implementation/spec/test edits; no extra reviewer; Boat active expiry12:22Z.
