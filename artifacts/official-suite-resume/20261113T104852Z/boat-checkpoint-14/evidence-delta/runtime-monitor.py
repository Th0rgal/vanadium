import pathlib,time,datetime,json,subprocess,os,signal
r=pathlib.Path('/var/lib/orb-node/work/official-suite-resume');e=r/'evidence'
names=['ragger-tests-nanosp-1800-full','ragger-tests-nanox-1800-full']
deadline=datetime.datetime(2026,11,13,14,20,tzinfo=datetime.timezone.utc);next_checkpoint=0
receipt={'pid':os.getpid(),'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'active_deadline_utc':deadline.isoformat(),'expiry_epoch':1794579747,'runs':names,'signals_sent':[]}
(e/'monitor-extension-active.json').write_text(json.dumps(receipt,indent=2))
while True:
 now=datetime.datetime.now(datetime.timezone.utc);done=all((e/(n+'.json')).exists() for n in names)
 print(json.dumps({'utc':now.isoformat(),'pid':os.getpid(),'active_deadline_utc':deadline.isoformat(),'completed':[n for n in names if (e/(n+'.json')).exists()],'tails':{n:(e/(n+'.stdout')).read_text()[-300:] if (e/(n+'.stdout')).exists() else None for n in names}}),flush=True)
 if time.monotonic()>=next_checkpoint or done or now>=deadline:
  p=subprocess.run(['python3',str(e/'live-checkpoint.py')],capture_output=True,text=True);print(p.stdout,p.stderr,flush=True);next_checkpoint=time.monotonic()+300
 if done:break
 if now>=deadline:
  for name in names:
   q=e/(name+'.active.json')
   if q.exists() and not (e/(name+'.json')).exists():
    active=json.loads(q.read_text());pid=active['child_pid']
    try:
     cmd=(pathlib.Path('/proc')/str(pid)/'cmdline').read_text()
     if 'pytest' in cmd and str(r) in cmd:
      os.kill(pid,signal.SIGINT);receipt['signals_sent'].append({'pid':pid,'at':now.isoformat()});print('TTL safety SIGINT pytest '+str(pid),flush=True)
    except (ProcessLookupError,FileNotFoundError):pass
  (e/'monitor-extension-active.json').write_text(json.dumps(receipt,indent=2));time.sleep(15);subprocess.run(['python3',str(e/'live-checkpoint.py')]);break
 time.sleep(30)
receipt['ended_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();(e/'monitor-extension-active.json').write_text(json.dumps(receipt,indent=2))
