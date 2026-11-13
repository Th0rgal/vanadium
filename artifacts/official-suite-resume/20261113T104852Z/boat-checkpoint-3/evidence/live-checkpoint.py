import pathlib,json,tarfile,hashlib,datetime,xml.etree.ElementTree as ET,shutil,re
r=pathlib.Path('/var/lib/orb-node/work/official-suite-resume');e=r/'evidence'
names={'ctest_full':'ctest-full','mainnet_nanosp':'mainnet-nanosp','mainnet_nanox':'mainnet-nanox2','testnet_nanosp':'ragger-tests-nanosp3','testnet_nanox':'ragger-tests-nanox','bitcoin_rust_app':'bitcoin-app-resolved','bitcoin_rust_common':'bitcoin-common-resolved','root_common_canary':'common-canary'}
results={};attempts={}
for p in e.glob('*.json'):
 try:d=json.loads(p.read_text())
 except Exception:continue
 if 'argv' not in d:continue
 name=p.stem;q=e/(name+'.xml');s={'exit':d['exit'],'pass':None,'fail':None,'skip':None,'errors':None,'deselected':None}
 if q.exists():
  x=ET.parse(q).getroot();cases=list(x.iter('testcase'));s.update({'pass':sum(not any(c.find(k) is not None for k in ['failure','error','skipped']) for c in cases),'fail':sum(c.find('failure') is not None for c in cases),'skip':sum(c.find('skipped') is not None for c in cases),'errors':sum(c.find('error') is not None for c in cases),'deselected':0,'reported_cases':len(cases)})
  txt=(e/(name+'.stdout')).read_text();m=re.search(r'(\d+) deselected',txt)
  if m:s['deselected']=int(m.group(1))
 attempts[name]=s
for key,name in names.items():results[key]=dict(attempts.get(name,{'status':'RUNNING_OR_NOT_RUN','pass':None,'fail':None,'skip':None,'errors':None,'deselected':None,'exit':None}),log=name)
for sub in ['app','common']:shutil.copy2(r/f'vanadium/apps/bitcoin/{sub}/Cargo.lock',e/f'bitcoin-{sub}.Cargo.lock')
(e/'counts.json').write_text(json.dumps({'status':'IN_PROGRESS','time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'selected_runs':results,'attempts':attempts,'ctest_enumerated':31,'exclusions_added':[],'notes':['Source worktree attempt failed Ragger .git-directory discovery; moved to exact standalone clone without editing tests.','Default-port overlapping testnet attempt interrupted after mainnet collision; full isolated reruns supersede it, all raw results retained.','Mainnet suite is legacy Speculos fixtures in tests_mainnet, not Ragger plugin; both devices still ran full directory slow=2.','Tests pure checks may pass even when session backend setup fails; never certify whole suite from those passes.']},indent=2))
(e/'CURRENT.md').write_text('''# IN_PROGRESS — current checkpoint

Current evidence supersedes earlier missing-before-provisioning blockers in REPORT.md. The user authorized absent nested lockfile generation and authentic native provisioning.

Full native CTest completed: all31 enumerated targets passed, SpeculosON; raw JSON enumeration, stdout and JUnit retained. Mainnet full directory completed2/2 passed on each nanosp/nanox, slow2 enabled, no exclusions. Full testnet282 collected per device now running on explicit isolated Speculos API ports5001/5101. Separate real Core32.1 nodes use default regtestRPC18443 and alternate19443; launcher bitcoind-nanox.sh only execs authentic Core with port configuration, no fake responses. Its private datadir isolates blockchain/wallet state. Initial worktree Ragger discovery errors and overlapping emulator attempt remain archived as unsuccessful/superseded attempts, not discarded. Read counts.json for completed attempts; active runs keep counts null until completion.

Authentic SDKv27.1.7 SHA9ea0fae9b40bb91e7c4f94bb0e9b8cf22df36306 from builder98693c3b63446779677d35bd7ed7c5923949ab01; public CMocka1.1.7, QEMU8.2.2, newlib/GCC ARM and LLVM21 packages privately extracted. LLVM18 IR parse failure resolved by upgrading compiler, not editing embedded IR. Real Core32.1 installed and archive verified by upstream script. App mainnet/testnet worktrees built both nanosp/nanox with DEBUG0, no autoapprove. Testnet built artifacts copied byte-for-byte into standalone app clone because Ragger fails worktree .git files; SHA256 recorded. Full Python requirements installed unmodified after privately relocating extracted libtoolize data paths. No application or spec weakening.

Bitcoin app/common private locks generated from unchanged manifests; archived and hashed in provisioned-versions.stdout. Both locked builds reached FFI but installed lean-native0.5.0 lacks emit-freestanding-c-lib; authentic public current emitter15676ea244a08d386f8047c4bbfe0416692d1089 is building privately. Public emitter build succeeded (366 build jobs sequentially scheduled, 1 worker); baseline host emission exits1 with Unsupported exported tuple parameter witSpk in BitcoinLedger.FreestandingKernels.llbCheckDualUtxo. This real public emitter/source compatibility failure blocks dependent Rust execution. No baseline/source/ABI rewrite or fabricated FFI. Parent needs a compatible authentic emitter revision or baseline-derived artifacts. Root existing Cargo.lock unchanged (139326fa0b3bd5d75ba9447549493fd135330d1f2bf51a0d9c95ee50a04e7546). Root common exact locked canary remains blocked by lock inconsistency. No untracked root lock regeneration. CandidateA never substituted for pinned Lean baselinef68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb.

No source/test/spec edits. Full upstream skip rules retained; runtime skip reasons will be recorded from -ra. Source static skip locations in final-inventory and prerequisite-source-details logs. No selected exclusions/deselections, no golden regeneration. All build/test logs, exact env/argv/cwd/exits and generated lockfiles only; no caches/binaries in archive. Max jobs4, Rust1; no privileged operations, credentials, Docker bypass, other models or subagents. TTL12:22Z unchanged. No overall PASS claim while suites incomplete.
''')
with tarfile.open(r/'evidence.tar.gz','w:gz') as t:t.add(e,arcname='evidence')
p=r/'evidence.tar.gz';assert p.stat().st_size<20*1024*1024;print(json.dumps({'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'path':str(p),'selected_runs':results}))
