import os
import shutil
import tempfile

print("tempdir is %s" % tempfile.gettempdir())

############
tmpdir1 = tempfile.mkdtemp("", "prysk-tests-")
print("tmpdir1: %s" % tmpdir1)
os.system("git init $dd --quiet --initial-branch=main" % tmpdir1)
os.system("pushd %s && mkdir foo && touch foo/bar.txt && popd" % tmpdir1)
os.system("ls -al %s" % tmpdir1)
os.system("ls -al %s/.git" % tmpdir1)
os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" config user.email \"turbo-test@example.com\"" % (tmpdir1, tmpdir1))
os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" config user.name \"Turbo Test\"" % (tmpdir1, tmpdir1))
os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" add ." % (tmpdir1, tmpdir1))
os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" commit -m \"Initial\" --quiet" % (tmpdir1, tmpdir1))

############
tmpdir2 = tempfile.mkdtemp("", "prysk-tests-")
print("tmpdir2: %s" % tmpdir2)
os.system("pushd %s && mkdir foo && touch foo/bar.txt && popd" % tmpdir2)
os.system("ls -al %s/foo" % tmpdir2)

############

print("Deleting %s", tmpdir1)
shutil.rmtree(tmpdir1)
print("Deleting %s", tmpdir1)
shutil.rmtree(tmpdir2)
