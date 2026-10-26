"""Check the exact public runtime and localization without CK3 or third-party packages."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
def check():
 expected=json.loads((ROOT/'publishing/runtime-manifest.json').read_text(encoding='utf8'))
 root=ROOT/'mod/maa_war_planner'
 actual={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()}
 assert actual==expected['runtime_sha256'],'Runtime differs from reviewed release'
 locales={}
 for directory in (root/'localization').iterdir():
  values={}
  for p in directory.glob('*.yml'):
   assert p.read_bytes().startswith(b'\xef\xbb\xbf'),p
   for line in p.read_text(encoding='utf-8-sig').splitlines()[1:]:
    if not line.strip() or line.lstrip().startswith('#'):continue
    m=re.fullmatch(r'\s+([\w.-]+):(?:\d+)?\s+"((?:\\.|[^"\\])*)"\s*(?:#.*)?',line)
    assert m,(p,line)
    assert m[1] not in values,('duplicate',p,m[1])
    values[m[1]]=m[2]
  assert len(values)==606,(directory,len(values))
  assert values['mwp_info_title'].startswith('Strategist Assistant'),directory
  locales[directory.name]=set(values)
 assert len(locales)==9 and all(v==locales['english'] for v in locales.values())
 return {'status':'STATIC_PASS','runtime_files':len(actual),'languages':len(locales),'keys_per_language':606}
if __name__=='__main__':print(json.dumps(check()))
