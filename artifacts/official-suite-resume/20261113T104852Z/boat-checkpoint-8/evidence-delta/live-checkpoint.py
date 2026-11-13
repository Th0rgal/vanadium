import pathlib,json,tarfile,hashlib,datetime,xml.etree.ElementTree as ET,shutil,re
r=pathlib.Path('/var/lib/orb-node/work/official-suite-resume');e=r/'evidence'
names={'ctest_full':'ctest-full','mainnet_nanosp':'mainnet-nanosp','mainnet_nanox':'mainnet-nanox2','testnet_nanosp':'ragger-tests-nanosp3','testnet_nanox':'ragger-tests-nanox','bitcoin_rust_app':'bitcoin-app-with-ffi','bitcoin_rust_common':'bitcoin-common-with-ffi','root_common_canary':'common-canary','testnet_nanosp_long':'ragger-tests-nanosp-long','testnet_nanox_long':'ragger-tests-nanox-long','diagnostic_512_nanosp':'diagnostic-512-nanosp','diagnostic_512_nanox':'diagnostic-512-nanox','testnet_nanosp_final':'ragger-tests-nanosp-final2','testnet_nanox_final':'ragger-tests-nanox-final','diagnostic_512_nanosp_retry':'diagnostic-512-nanosp-retry','diagnostic_512_nanox_retry':'diagnostic-512-nanox-retry'}
results={};attempts={}
for p in e.glob('*.json'):
 try:d=json.loads(p.read_text())
 except Exception:continue
 if 'argv' not in d or 'exit' not in d:continue
 name=p.stem;q=e/(name+'.xml');s={'exit':d['exit'],'pass':None,'fail':None,'skip':None,'errors':None,'deselected':None}
 if q.exists():
  x=ET.parse(q).getroot();cases=list(x.iter('testcase'));s.update({'pass':sum(not any(c.find(k) is not None for k in ['failure','error','skipped']) for c in cases),'fail':sum(c.find('failure') is not None for c in cases),'skip':sum(c.find('skipped') is not None for c in cases),'errors':sum(c.find('error') is not None for c in cases),'deselected':0,'reported_cases':len(cases)})
  txt=(e/(name+'.stdout')).read_text();m=re.search(r'(\d+) deselected',txt)
  if m:s['deselected']=int(m.group(1))
 txt=(e/(name+'.stdout')).read_text()
 matches=re.findall(r'test result: (?:ok|FAILED)\. (\d+) passed; (\d+) failed; (\d+) ignored; (\d+) measured; (\d+) filtered out',txt)
 if matches:
  rows=[[int(v) for v in m] for m in matches];s.update({'pass':sum(v[0] for v in rows),'fail':sum(v[1] for v in rows),'skip':sum(v[2] for v in rows),'deselected':sum(v[4] for v in rows),'errors':0,'rust_result_groups':rows})
 s['execution_complete'] = d['exit'] in [0,1]
 if 'pytest' in d['argv']:s['suite_complete'] = d['exit'] in [0,1] and '.' in d['argv']
 attempts[name]=s
for key,name in names.items():results[key]=dict(attempts.get(name,{'status':'RUNNING_OR_NOT_RUN','pass':None,'fail':None,'skip':None,'errors':None,'deselected':None,'exit':None}),log=name)
for sub in ['app','common']:shutil.copy2(r/f'vanadium/apps/bitcoin/{sub}/Cargo.lock',e/f'bitcoin-{sub}.Cargo.lock')
(e/'counts.json').write_text(json.dumps({'status':'IN_PROGRESS','time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'selected_runs':results,'attempts':attempts,'ctest_enumerated':31,'exclusions_added':[],'notes':['Source worktree attempt failed Ragger .git-directory discovery; moved to exact standalone clone without editing tests.','Default-port overlapping testnet attempt interrupted after mainnet collision; full isolated reruns supersede it, all raw results retained.','Mainnet suite is legacy Speculos fixtures in tests_mainnet, not Ragger plugin; both devices still ran full directory slow=2.','Tests pure checks may pass even when session backend setup fails; never certify whole suite from those passes.']},indent=2))
report = """# Current official-suite execution report

Status: IN_PROGRESS. This report supersedes historical-before-checkpoint3-REPORT.md and other historical attempts. Counts below are executed results; incomplete runs remain null.

Full native CTest: 31 target-level passes, zero failures/skips; upstream 30 plus one added target. Full CMocka output is native-ctest/LastTest.log; CMakeCache.txt is included alongside it. JUnit truncation does not establish assertion-level counts. CTest was not repeated.

Full mainnet: 2 passed on nanosp and 2 passed on nanox, slow=2. These use upstream legacy Speculos fixtures. Full locked Bitcoin Rust: app 90 passed; common 85 passed (81 unit, 4 integration). No test exclusions added.

Root common locked exact canary exits101 before compilation because the unchanged upstream root lock needs an update (cargo-vnd/rhai_codegen dependency edge). This is a local manifest/lock consistency blocker, not a Bitcoin behavior failure. Safe remediation requires parent reconciliation of that existing lock or a proven matching toolchain. Root lock SHA256 139326fa0b3bd5d75ba9447549493fd135330d1f2bf51a0d9c95ee50a04e7546 remains unchanged.

Full testnet runs collect282 per device with slow=2. First full attempts used timeout300 and show a512-input failure marker but were interrupted before final traceback/exit/JUnit. At11:44Z no prior suite/queue/diagnostic processes remained and prior session IDs were unknown; cause is not established. These incomplete attempts have null counts/exit, not a fabricated exit. Fresh timeout1800 full attempts were explicitly interrupted after about60 seconds to fit existing TTL (exit2 and partial results retained). Fresh full timeout300 attempts then started11:46Z; isolated exact512 diagnostics use1800. The first nanosp restart was interrupted after observing a leftover Core node from interrupted session setup; replacement final2 uses fresh22443/22444 ports and datadir. No exclusions/assertion/skip-rule changes. A timeout remains failure, never PASS. Read per-run execution_complete/suite_complete; interrupted observed cases do not cover the full collection. Separate interrupted exact512 diagnostics are narrow runs and never counted as full-suite acceptance. Read counts.json and per-run raw logs for actual completion and outcomes. All incomplete counts remain null. Upstream skips remain unchanged and reasons appear in raw -ra summaries.

Authentic prerequisites were provisioned privately: SDK v27.1.7, LLVM21.1.8, CMocka1.1.7, QEMU8.2.2, Core32.1 (upstream setup verification), Speculos/Ragger. Public turbo-lean branch feat/freestanding-flat-ptr-loops at8c3503fa0df74fafcd7a3b91e4319606985b7198 generated baseline f68864d1f2af8fd9f2ca26acddb5f0abd3e80bcb host FFI (45 exports, no undefined). Earlier missing-prerequisite/emitter attempts are historical, superseded by successful provisioning. Candidate A was never substituted. Extracted private libtoolize data paths were relocated to its authentic private data directory; no tests/assertions changed.

Only new private nested Cargo.lock files were generated from unchanged manifests; copies, hashes, and nested-lockfiles.patch are included for parent signing. Tracked source diffs remain empty. No credentials, push, privileges, Docker bypass, other models, or subagents. No overall PASS claim. VM TTL remains12:22Z.

## Selected completed/incomplete runs

"""
report += '```json\n' + json.dumps(results,indent=2) + '\n```\n'
report += '\n## Configure attempts (per-run, not aggregated)\n\n'
for name in ['app-configure','ctest-native-configure','ctest-llvm21-configure']:
 if name in attempts: report += f"{name}: exit {attempts[name]['exit']}; see exact argv and logs.\n\n"
(e/'REPORT.md').write_text(report)
(e/'CURRENT.md').write_text(report)

with tarfile.open(r/'evidence.tar.gz','w:gz') as t:t.add(e,arcname='evidence')
p=r/'evidence.tar.gz';assert p.stat().st_size<20*1024*1024;print(json.dumps({'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'path':str(p),'selected_runs':results}))
