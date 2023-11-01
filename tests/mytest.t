Setup
  $ if [[ "$OSTYPE" == "msys" ]]; then cygpath fixture/package.json; else echo $(basename $TESTDIR/fixture)/package.json; fi
  fixture(/|\\)package.json (re)