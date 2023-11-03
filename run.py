import os
import shutil
import tempfile

tmpdir = tempfile.mkdtemp("", "prysk-tests-", ".")
print("Using temporary directory: %s" % tmpdir)

# initialize a git repoository in the temporary directory
os.system("git init $dd --quiet --initial-branch=main" % tmpdir)
os.system("pushd %s && touch foo && popd" % tmpdir)
os.system("ls -al %s" % tmpdir)
os.system("ls -al %s/.git" % tmpdir)

os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" config user.email \"turbo-test@example.com\"" % (tmpdir, tmpdir))
os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" config user.name \"Turbo Test\"" % (tmpdir, tmpdir))

os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" add ." % (tmpdir, tmpdir))
os.system("git --git-dir=\"%s/.git\" --work-tree=\"%s\" commit -m \"Initial\" --quiet" % (tmpdir, tmpdir))


print("Deleting %s", tmpdir)
shutil.rmtree(tmpdir)
