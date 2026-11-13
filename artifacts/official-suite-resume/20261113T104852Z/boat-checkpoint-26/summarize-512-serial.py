import pathlib,json,datetime,os,hashlib,gzip,tarfile,io
R=pathlib.Path('/var/lib/orb-node/work/official-suite-resume');E=R/'evidence';T=R/'transfer';N='diagnostic-512-nanox-serial-trace'
a=[json.loads(x) for x in (E/(N+'.progress.jsonl')).read_text().splitlines()];hz=os.sysconf('SC_CLK_TCK');intervals=[]
for before,after in zip(a,a[1:]):
 old={p['pid']:p for p in before['processes']};ps=[]
 for p in after['processes']:
  if p['pid'] not in old:continue
  x=old[p['pid']]['stat'].split(') ',1)[1].split();y=p['stat'].split(') ',1)[1].split()
  if x[19]!=y[19]:continue
  ps.append({'pid':p['pid'],'cmdline':p['cmdline'],'user_seconds':(int(y[11])-int(x[11]))/hz,'system_seconds':(int(y[12])-int(x[12]))/hz})
 intervals.append({'start_utc':before['utc'],'end_utc':after['utc'],'requests_delta':after['log_progress']['requests']-before['log_progress']['requests'],'responses_delta':after['log_progress']['responses']-before['log_progress']['responses'],'process_cpu':ps})
record=E/(N+'.json');d={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'complete':record.exists(),'receipt':json.loads(record.read_text()) if record.exists() else None,'last_progress':a[-1],'intervals':intervals,'limitations':['strace and DEBUG logging can alter timing; diagnostic only','APDU counts are log-based, not independent wire capture','no guest stack captured; exit255 caller cannot be inferred from message alone','historical full-suite failures and runner process loss remain separate']};(E/(N+'.analysis.json')).write_text(json.dumps(d,indent=2));print(json.dumps({'complete':d['complete'],'latest':a[-1]['utc'],'progress':a[-1]['log_progress']}))
