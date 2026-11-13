# Host navigation interruption candidate

Baseline guest, SDK, official tests, selection, timeout and review assertions are unchanged. Guest GDB captured exception5 in io_event while process_interruption awaited host data during display_external_outputs, followed by app_exit requesting255. The GDB script then exceeded the stack boundary during an optional read; its subsequent process exits are observer-affected and distinct from native255 evidence.

The app Ragger adapter temporarily raises non-success responses during an async exchange so lateE000 unwinds navigation to the existing client interpreter. It preserves the current request and substep cursor across interruptions and restores the prior transport policy in finally. Final successful commands must still satisfy the existing required-review count.

Ragger navigator previously leaked a ticker pause whenever navigation raised. Both navigation methods now resume in finally, including nested navigation. This generic cleanup fix is in a separate patch against publicRaggerv1.47.4 at75a33226dc92d9af964c676a96bb99183bc38f5b. Runtime backend source matches the installed pinned package byte-for-byte. No installedsitepackage mutation.

Meaningful regressions: actual backend late response path, review cursor not replayed/skipped, mandatory-review guard, unrelated error propagation, response-policy restoration, tickercleanup in both navigationmethods. Original v3:3failed3passed; candidate6passed. Upstream navigator33passed; including upstream-style newcleanupregression34passed. Narrow512 live validation pending; no fullsuite candidate acceptance yet.

Patch paths: evidence/bitcoin-navigation-interruption-with-regression.patch and evidence/ragger-navigation-ticker-with-regression.patch. Exactindex transfer/navigation-fix-index.json. Baseline source locks untouched. Speculoscallbackcandidate retained explicitly; this is not LeanCandidateA.
