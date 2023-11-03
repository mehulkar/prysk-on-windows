import os
import shutil
import tempfile

tmpdir = tempfile.mkdtemp("", "prysk-tests-")
print("tmpdir: %s" % tmpdir)
os.system("git init %s --quiet --initial-branch=main" % tmpdir)
os.system("pushd %s && mkdir foo && touch foo/bar.txt && popd" % tmpdir)
os.system("ls -al %s" % tmpdir)
os.system("ls -al %s/.git" % tmpdir)
os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" config user.email \"test@example.com\"" % (tmpdir, tmpdir))
os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" config user.name \"Test Test\"" % (tmpdir, tmpdir))
os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" add ." % (tmpdir, tmpdir))
os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" commit -m \"Initial\" --quiet" % (tmpdir, tmpdir))


print("Deleting tmpdir: %s" % tmpdir)
shutil.rmtree(tmpdir)
