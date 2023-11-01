Setup
  $ if [[ "$OSTYPE" == "msys" ]]; then cygpath fixture/package.json; else ls fixture/package.json; fi
  fixture(/|\\)package.json (re)