import pathlib,json,tarfile,hashlib
r=pathlib.Path('/var/lib/orb-node/work/official-suite-resume');e=r/'evidence'
p=e/'REPORT.md';old=p.read_text();(e/'checkpoint-1-REPORT.md').write_text(old)
update='''# Updated BLOCKED checkpoint — public sibling supplied and pinned

The user supplied the anonymous public Lean source URL. Cloned https://github.com/Th0rgal/lean-ledger-bitcoin.git as sibling of vanadium and checked out detached f68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb, verified exactly. Candidate A 092bb97 was not substituted. The prior missing sibling source blocker is resolved; checkpoint-1-REPORT.md preserves the earlier state only.

Fresh separate invocations from apps/bitcoin/app and apps/bitcoin/common, each cargo +stable test --locked, both exit 101 before compilation: cannot create the respective absent Cargo.lock because --locked prevents this. app and common each declare their own workspace; apps/bitcoin has no root workspace manifest. Parent must provide reviewed lockfiles/source revisions or explicitly authorize a separate dependency resolution step before these can run locked. Neither --locked was removed nor any lockfile generated.

Additional static prerequisite observed: neither ffi/vanadium/build/host/liblean_ledger_bitcoin.a nor matching .ll exists in the public baseline checkout. build.rs requires that host archive, attempts authentic lean-native emission if available, and otherwise panics. No Cargo invocation reached this build script because lockfile validation stopped earlier. The source generator is scripts/build-freestanding.sh; its documented tool is a turbo-lean lean-native driver, not ordinary upstream lean/lake. No generated FFI was fabricated, no candidate artifacts reused and no assertion/spec changes. Missing archive is an observed later prerequisite, not a claimed compiler failure. See ffi-artifacts and ffi-prerequisite-check logs for exact source and file absence. Parent can provide baseline-derived authenticated artifacts or the exact public emitter revision/build recipe.

Common canary lock inconsistency, Docker permission denial and missing authentic BOLOS_SDK remain as previously recorded below. All official execution counts remain null. Nothing passed. Sources in all three checkouts remain clean; upstream Vanadium Cargo.lock hash unchanged. No patches/bundle required for unchanged sources.

Bitcoin Core requirement confirmed directly from public tests/setup_script.sh: version 32.1, archive SHA256 61545c17c3120fb7412f896d248b11993af04ec8817aad3649c55b2afb044963; script verifies download before extraction. It was inspected, not run, since dependent device testing remains blocked. Mainnet bitcoin and testnet bitcoin_testnet builds remain distinct and neither was built. No new exclusions.

## Original checkpoint context (superseded where stated above)

'''
p.write_text(update+old)
c=json.loads((e/'counts.json').read_text());c['suites']['bitcoin_rust_app'].update(status='BLOCKED_MISSING_LOCKFILE',exit=101);c['suites']['bitcoin_rust_common'].update(status='BLOCKED_MISSING_LOCKFILE',exit=101);c['lean_baseline']='f68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb';(e/'counts.json').write_text(json.dumps(c,indent=2))
with tarfile.open(r/'evidence.tar.gz','w:gz') as t:t.add(e,arcname='evidence')
p=r/'evidence.tar.gz';assert p.stat().st_size<20*1024*1024
print(json.dumps({'archive':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'BLOCKED'}))
