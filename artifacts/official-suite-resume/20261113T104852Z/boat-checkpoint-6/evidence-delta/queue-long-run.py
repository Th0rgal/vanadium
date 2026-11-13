import sys,pathlib,time,json,subprocess,datetime
r=pathlib.Path('/var/lib/orb-node/work/official-suite-resume');e=r/'evidence';device=sys.argv[1];prior='ragger-tests-nanosp3' if device=='nanosp' else 'ragger-tests-nanox';new='ragger-tests-'+device+'-long'
print(json.dumps({'awaiting_complete_attempt':prior,'next_complete_run':new,'change_only':'timeout300 to1800; same full directory and slow2','start_deadline_utc':'2026-11-13T11:50:00Z'}),flush=True)
while not (e/(prior+'.json')).exists():
 if datetime.datetime.now(datetime.timezone.utc)>=datetime.datetime(2026,11,13,11,50,tzinfo=datetime.timezone.utc):
  print('Not starting: remaining TTL insufficient for a fresh slow full run',flush=True);sys.exit(124)
 time.sleep(2)
d=json.loads((e/(prior+'.json')).read_text());argv=d['argv'];argv=['--timeout=1800' if a=='--timeout=300' else ('--junitxml='+str(e/(new+'.xml'))) if a.startswith('--junitxml=') else a for a in argv]
print(json.dumps({'prior_exit':d['exit'],'next_cwd':d['cwd'],'next_argv':argv}),flush=True)
p=subprocess.run([sys.executable,str(e/'run.py'),new,d['cwd'],*argv]);sys.exit(p.returncode)
