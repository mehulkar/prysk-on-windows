import os
import shutil
import tempfile

tmpdir = os.environ["PRYSK_TEMP"] = tempfile.mkdtemp("", "prysk-tests-")
print("Using temporary directory: %s" % tmpdir)

shutil.rmtree(tmpdir)
