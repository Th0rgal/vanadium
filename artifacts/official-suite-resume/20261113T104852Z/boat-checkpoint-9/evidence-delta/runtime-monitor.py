import pathlib,time,datetime,json,subprocess,os,signal
r=pathlib.Path('/var/lib/orb-node/work/official-suite-resume');e=r/'evidence'
names=['ragger-tests-nanosp-final2','ragger-tests-nanox-final','diagnostic-512-nanosp-retry','diagnostic-512-nanox-retry']
pids=[319986,314351,316913,317030]
deadline=datetime.datetime(2026,11,13,12,20,tzinfo=datetime.timezone.utc);next_checkpoint=0
while True:
 now=datetime.datetime.now(datetime.timezone.utc); done=all((e/(n+'.json')).exists() for n in names)
 print(json.dumps({'utc':now.isoformat(),'completed':[n for n in names if (e/(n+'.json')).exists()],'tails':{n:(e/(n+'.stdout')).read_text()[-240:] for n in names}}),flush=True)
 if time.monotonic()>=next_checkpoint or done or now>=deadline:
  p=subprocess.run(['python3',str(e/'live-checkpoint.py')],capture_output=True,text=True);print(p.stdout,p.stderr,flush=True);next_checkpoint=time.monotonic()+300
 if done:break
 if now>=deadline:
  for pid in pids:
   try:
    cmd=pathlib.Path('/proc')/str(pid)/'cmdline'
    if 'pytest' in cmd.read_text() and str(r) in cmd.read_text():os.kill(pid,signal.SIGINT);print('TTL safety SIGINT pytest '+str(pid),flush=True)
   except ProcessLookupError:pass
   except FileNotFoundError:pass
  time.sleep(15);subprocess.run(['python3',str(e/'live-checkpoint.py')]);break
 time.sleep(30)
