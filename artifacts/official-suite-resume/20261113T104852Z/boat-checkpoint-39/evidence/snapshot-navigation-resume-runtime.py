import pathlib,json,datetime,hashlib,re
R=pathlib.Path('/var/lib/orb-node/work/official-suite-resume');E=R/'evidence';rows=[]
for dev in ['nanosp','nanox']:
 stem='ragger-navigation-resume-full-'+dev;rec=json.loads((E/(stem+'.active.json')).read_text());pid=rec['pid'];row={'device':dev,'pid':pid,'completed':(E/(stem+'.json')).exists()}
 if not row['completed']:
  p=pathlib.Path('/proc')/str(pid)
  try:
   st=(p/'stat').read_text();f=st[st.rfind(')')+2:].split();row.update(state=f[0],utime_ticks=int(f[11]),stime_ticks=int(f[12]),starttime_ticks=int(f[19]))
   # Opening own pytest capture file is read-only; no UI, socket, signal or process mutation.
   b=(p/'fd/2').read_bytes();s=b.decode(errors='replace');req=re.findall(r'ragger\.apdu_logger - => ([0-9a-f]+)',s);resp=re.findall(r'ragger\.apdu_logger - <= ([0-9a-f]+)',s);row.update(capture_bytes=len(b),capture_sha256=hashlib.sha256(b).hexdigest(),current_capture_requests=len(req),current_capture_responses=len(resp),last_request=req[-1] if req else None,last_response=resp[-1] if resp else None)
  except OSError as error:row['read_error']=str(error)
 rows.append(row)
d={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'classification':'READ_ONLY_PROCESS_CURRENT_CAPTURE_SNAPSHOT_NOT_TERMINAL_COUNTS','counts_scope':'Current pytest capture only; resets per test; never sum replay or resets','rows':rows}
with (E/'navigation-resume-runtime-snapshots.jsonl').open('a') as f:f.write(json.dumps(d)+'\n')
p=R/'transfer/navigation-resume-runtime-latest.json';tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(d,indent=2));tmp.replace(p);print(json.dumps(d))
