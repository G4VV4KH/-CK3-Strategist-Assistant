import importlib.util
from pathlib import Path
import unittest
class PublicRuntimeTest(unittest.TestCase):
 def test_release_runtime_and_languages(self):
  p=Path(__file__).resolve().parents[1]/'tools/verify_runtime.py'
  spec=importlib.util.spec_from_file_location('verify_runtime',p)
  m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
  self.assertEqual(m.check()['status'],'STATIC_PASS')
if __name__=='__main__':unittest.main()
