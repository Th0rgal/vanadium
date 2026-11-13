import pathlib,json,datetime,xml.etree.ElementTree as ET
R=pathlib.Path('/var/lib/orb-node/work/official-suite-resume');E=R/'evidence';T=R/'transfer'
p=T/'navigation-full-index.json';d=json.loads(p.read_text());d['utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
for device,run in d['runs'].items():
 stem='ragger-navigation-resume-full-'+device;receipt=E/(stem+'.json');out=(E/(stem+'.stdout')).read_text();run['stdout_bytes']=(E/(stem+'.stdout')).stat().st_size;run['tail']=out[-650:];run['observed_failure_markers']=[x for x in out.splitlines() if ' FAILED ' in x];run['observed_512_pass']=f'test_sign_psbt_singlesig_wpkh_512to256[{device}-{device}] PASSED' in out
 if receipt.exists():
  rec=json.loads(receipt.read_text());run.update(status='COMPLETED',exit=rec['exit'],ended_utc=rec['ended_utc'])
  cases=list(ET.parse(E/(stem+'.xml')).getroot().iter('testcase'));run['counts']={'pass':sum(not any(c.find(k) is not None for k in ['failure','error','skipped']) for c in cases),'fail':sum(c.find('failure') is not None for c in cases),'skip':sum(c.find('skipped') is not None for c in cases),'errors':sum(c.find('error') is not None for c in cases),'deselected':0,'exit':rec['exit'],'reported_cases':len(cases)}
if all(x['status']=='COMPLETED' for x in d['runs'].values()):d['classification']='FULL_BOTH_TERMINAL_CHECK_COUNTS_NOT_GLOBAL_ACCEPTANCE'
tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(d,indent=2));tmp.replace(p)
print(json.dumps({'utc':d['utc'],'runs':{k:{'status':v['status'],'tail':v['tail'][-220:],'failures':v['observed_failure_markers'],'counts':v['counts']} for k,v in d['runs'].items()}}))
