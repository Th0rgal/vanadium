import pathlib,hashlib,json,datetime,os
R=pathlib.Path('/var/lib/orb-node/work/official-suite-resume')
def pytest_sessionstart(session):
    import ragger_bitcoin.ragger_bitcoin as adapter
    import ragger.navigator.navigator as navigator
    import ragger.backend.speculos as backend
    import speculos.mcu.seproxyhal as speculos
    rows=[]
    for module,expected in [(adapter,R/'app-navigation-fix/ragger_bitcoin/ragger_bitcoin.py'),(navigator,R/'ragger-navigation-fix/src/ragger/navigator/navigator.py'),(backend,R/'ragger-navigation-fix/src/ragger/backend/speculos.py'),(speculos,R/'speculos-candidate-runtime/speculos/mcu/seproxyhal.py')]:
        actual=pathlib.Path(module.__file__).resolve()
        assert actual==expected.resolve(),(actual,expected)
        rows.append({'module':module.__name__,'path':str(actual),'sha256':hashlib.sha256(actual.read_bytes()).hexdigest()})
    d={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'classification':'IN_PYTEST_SESSION_MODULE_PROVENANCE','modules':rows}
    p=R/'evidence'/os.environ.get('NAV_PROVENANCE_FILE','navigation-candidate-pytest-provenance.json');tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(d,indent=2));tmp.replace(p)
    print('VERIFIED_CANDIDATE_MODULES '+json.dumps(d),flush=True)
