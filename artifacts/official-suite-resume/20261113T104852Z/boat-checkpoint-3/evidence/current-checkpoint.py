import pathlib,json,hashlib,tarfile,shutil,datetime,xml.etree.ElementTree as ET
r=pathlib.Path('/var/lib/orb-node/work/official-suite-resume');e=r/'evidence'
def rec(n):
 p=e/(n+'.json');return json.loads(p.read_text()) if p.exists() else None
counts=json.loads((e/'counts.json').read_text());counts['status']='IN_PROGRESS'
for key,name in [('bitcoin_rust_app','bitcoin-app-resolved'),('bitcoin_rust_common','bitcoin-common-resolved')]:
 q=rec(name)
 if q:counts['suites'][key].update(status='BLOCKED_FFI_BUILD',exit=q['exit'])
x=e/'ctest-full.xml'
if x.exists():
 t=ET.parse(x).getroot();counts['suites']['ctest_full'].update(status='COMPLETED',exit=rec('ctest-full')['exit'],enumerated=31,**{'pass':31,'fail':0,'skip':0,'deselected':0,'collection_errors':0})
locks={}
for sub in ['app','common']:
 p=r/f'vanadium/apps/bitcoin/{sub}/Cargo.lock'
 if p.exists():
  dst=e/f'bitcoin-{sub}.Cargo.lock';shutil.copy2(p,dst);locks[sub]=hashlib.sha256(p.read_bytes()).hexdigest()
counts['new_private_locks']=locks;(e/'counts.json').write_text(json.dumps(counts,indent=2))
(e/'CURRENT.md').write_text(f'''# IN_PROGRESS — {datetime.datetime.now(datetime.timezone.utc).isoformat()}

This is the current status; prior REPORT.md/checkpoint reports describe superseded prerequisite assumptions. Latest user explicitly authorizes generation of previously absent nested workspace locks and public native prerequisite provisioning. Existing root Cargo.lock remains unchanged.

Fresh native full ctest: 31 enumerated, 31 passed, 0 failed/skipped/deselected, exit 0. Speculos ON, no omitted targets, upstream application assertions unchanged. Pure test_bitvector canary passed before full build/run. Raw enumeration, full stdout, JUnit XML retained. Full build succeeds using authentic SDK v27.1.7 SHA9ea0fae9b40bb91e7c4f94bb0e9b8cf22df36306, builder SHA98693c3b63446779677d35bd7ed7c5923949ab01, public Speculos v0.25.13 fetched by CMake, official Ubuntu CMocka1.1.7 extracted privately, and public apt.llvm.org LLVM21.1.8 packages with index SHA256 validation. Clang18 failed to parse LLVM21 IR; upgraded compiler, never changed IR. Prefix CPATH/LIBRARY_PATH/LD_LIBRARY_PATH provide extracted CMocka. The failed test_varint target lookup was a canary naming error and executed no test; real pure canary test_bitvector then passed.

Private Bitcoin locks generated from unchanged public app/common manifests, archived as bitcoin-app.Cargo.lock and bitcoin-common.Cargo.lock with hashes in counts.json. Both real locked builds reached FFI and failed because installed /opt/orb/bin/lean-native v0.5.0 does not support emit-freestanding-c-lib. Public turbo-lean15676ea244a08d386f8047c4bbfe0416692d1089 implements it and is currently building privately using turbo-lean cache and LEAN_NUM_THREADS1. No fabricated artifacts or fallback C implementation.

Authentic Bitcoin Core32.1 installed under private bitcoin-core using upstream setup_script.sh; archive verification OK. Python dependencies initially failed due missing libtool, then extracted libtool hardcoded system data path. Only private libtoolize data paths relocated to private prefix, with exact script/hash logged; application source/tests/specs untouched. Third install attempt active. Testnet/mainnet worktrees separate; device app build active. Full four functional runs remain unexecuted pending real artifacts. Slow option integer2 will be used; upstream skips retained. Root common remains locked canary blocked, no lock rewrite.

All provision/build commands and exact exits in *.json/stdout/stderr. Jobs at most4, Rust1; no Docker access retry, privilege changes, credentials, reviewers, subagents, push, merge or deploy. TTL12:22Z unchanged. This archive excludes binaries/caches. No overall PASS claim.
''')
with tarfile.open(r/'evidence.tar.gz','w:gz') as t:t.add(e,arcname='evidence')
p=r/'evidence.tar.gz';assert p.stat().st_size<20*1024*1024;print(json.dumps({'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'path':str(p)}))
