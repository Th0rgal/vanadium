import urllib.request,gzip,pathlib,hashlib,subprocess,json
r=pathlib.Path('/var/lib/orb-node/work/official-suite-resume');base='https://apt.llvm.org/noble/'
u=base+'dists/llvm-toolchain-noble-21/main/binary-amd64/Packages.gz';print(u,flush=True)
data=gzip.decompress(urllib.request.urlopen(u).read()).decode();records={}
for chunk in data.split('\n\n'):
 d={}
 for line in chunk.splitlines():
  if ': ' in line and not line.startswith(' '): k,v=line.split(': ',1);d[k]=v
 if 'Package' in d:records[d['Package']]=d
names=['libllvm21','libclang-cpp21','libclang-common-21-dev','libclang1-21','clang-21','llvm-21-linker-tools','libclang-rt-21-dev','lld-21','llvm-21','llvm-21-runtime','llvm-21-tools']
for n in names:
 d=records[n];p=r/'debs'/pathlib.Path(d['Filename']).name;print(json.dumps(d),flush=True)
 if not p.exists():urllib.request.urlretrieve(base+d['Filename'],p)
 assert hashlib.sha256(p.read_bytes()).hexdigest()==d['SHA256']
 subprocess.run(['dpkg-deb','-x',str(p),str(r/'prefix')],check=True)
print('extracted LLVM 21 packages',flush=True)
