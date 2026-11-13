import os,sys,json,subprocess,time,pathlib
root=pathlib.Path('/var/lib/orb-node/work/official-suite-resume'); ev=root/'evidence'
name,cwd,*argv=sys.argv[1:]
env=os.environ.copy()
env.update(CARGO_HOME=str(root/'cargo'),RUSTUP_HOME=str(root/'rustup'),CARGO_TARGET_DIR=str(root/'target'),CARGO_BUILD_JOBS='1',GIT_TERMINAL_PROMPT='0',TMPDIR=str(root/'tmp'),PIP_CACHE_DIR=str(root/'pip-cache'))
record={'cwd':cwd,'argv':argv,'env':{k:env[k] for k in ['CARGO_HOME','RUSTUP_HOME','CARGO_TARGET_DIR','CARGO_BUILD_JOBS','GIT_TERMINAL_PROMPT','TMPDIR','PIP_CACHE_DIR']},'started':time.time()}
with open(ev/(name+'.stdout'),'wb') as out,open(ev/(name+'.stderr'),'wb') as err:
 try: record['exit']=subprocess.run(argv,cwd=cwd,env=env,stdout=out,stderr=err).returncode
 except Exception as e: err.write(str(e).encode());record['exit']=127
record['ended']=time.time();(ev/(name+'.json')).write_text(json.dumps(record,indent=2));print(json.dumps(record));print((ev/(name+'.stdout')).read_text()[-12000:]);print((ev/(name+'.stderr')).read_text()[-12000:])
