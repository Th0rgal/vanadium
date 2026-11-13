import os,sys,json,subprocess,time,threading,pathlib,datetime,hashlib
R=pathlib.Path('/var/lib/orb-node/work/official-suite-resume'); E=R/'evidence'; N='diagnostic-512-nanox-serial-trace'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(name,data):
 p=E/name;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(data,indent=2));t.replace(p)
env=os.environ.copy();env.update(PATH=f"{R}/venv/bin:{R}/prefix/usr/bin:/usr/local/bin:/usr/bin:/bin",PYTHONPATH=str(R/'app-bitcoin'),PYTHONWARNINGS='ignore::DeprecationWarning',BITCOIND=str(R/'bitcoin-core/bitcoin-32.1/bin/bitcoind'),BITCOIN_DIRNAME=str(R/'core-512-serial-trace'),TMPDIR=str(R/'tmp'))
a=['strace','-f','-tt','-e','trace=process,signal','-o',str(E/(N+'.process.trace')),str(R/'venv/bin/python'),'-m','pytest','test_sign_psbt.py::test_sign_psbt_singlesig_wpkh_512to256','--device','nanox','--model','nanox','--speculos_port=5901','--enable_slow_tests=2','--timeout=1800','--log-level=DEBUG','-ra','-v','-s','--tb=short','--junitxml='+str(E/(N+'.xml'))]
rec={'cwd':str(R/'app-bitcoin/tests'),'argv':a,'env':{k:env[k] for k in ['PATH','PYTHONPATH','BITCOIND','BITCOIN_DIRNAME','TMPDIR']},'started_utc':now(),'actual_expiry_epoch':1794583347,'advisory_deadline_utc':'2026-11-13T15:20:00Z','deadline_action':'record only; never signal tests','signals_sent':[]}
counts={'requests':0,'responses':0,'last_request_utc':None,'last_response_utc':None,'lines':0};lock=threading.Lock()
with open(E/(N+'.stderr'),'wb') as err,open(E/(N+'.stdout'),'wb') as out:
 c=subprocess.Popen(a,cwd=rec['cwd'],env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE);rec['pid']=c.pid;write(N+'.active.json',rec)
 def reader(stream,dest):
  for line in iter(stream.readline,b''):
   dest.write(line);dest.flush()
   with lock:
    counts['lines']+=1
    if b'=> ' in line:counts['requests']+=1;counts['last_request_utc']=now()
    if b'<= ' in line:counts['responses']+=1;counts['last_response_utc']=now()
   if b'exit called' in line:
    with open(E/(N+'.exit-markers.jsonl'),'a') as f:f.write(json.dumps({'utc':now(),'line':line.decode(errors='replace').strip()})+'\n')
 threads=[threading.Thread(target=reader,args=(c.stdout,out)),threading.Thread(target=reader,args=(c.stderr,err))]
 for t in threads:t.start()
 while c.poll() is None:
  ps=[]
  for proc in pathlib.Path('/proc').glob('[0-9]*'):
   try:
    cmd=(proc/'cmdline').read_bytes().replace(b'\0',b' ').decode(errors='replace')
    if any(x in cmd for x in ['-m speculos','qemu-arm','-m pytest','--datadir='+env['BITCOIN_DIRNAME']]) and str(R) in cmd:
     ps.append({'pid':int(proc.name),'cmdline':cmd,'stat':(proc/'stat').read_text(),'cgroup':(proc/'cgroup').read_text()})
   except (OSError,ValueError):pass
  with lock:d=dict(counts)
  with open(E/(N+'.progress.jsonl'),'a') as f:f.write(json.dumps({'utc':now(),'processes':ps,'log_progress':d})+'\n')
  for _ in range(30):
   if c.poll() is not None:break
   time.sleep(1)
 for t in threads:t.join()
 rec.update(exit=c.returncode,ended_utc=now(),progress=counts);write(N+'.json',rec)
print(json.dumps(rec),flush=True)
