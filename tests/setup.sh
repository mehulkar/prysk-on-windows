#!/usr/bin/env bash

TARGET_DIR=$1

# TMPDIR=$(mktemp -d) # TODO: is this the issue?
THIS_DIR=$(dirname "${BASH_SOURCE[0]}")
cp -a "${THIS_DIR}/fixture/." "${TARGET_DIR}/"
git init "${TARGET_DIR}" --quiet --initial-branch=main

git --git-dir="${TARGET_DIR}/.git" --work-tree="${TARGET_DIR}" config user.email "turbo-test@example.com"
git --git-dir="${TARGET_DIR}/.git" --work-tree="${TARGET_DIR}" config user.name "Turbo Test"

echo "script-shell=$(which bash)" > "${TARGET_DIR}/.npmrc"
# We just created a new file. On Windows, we need to convert it to Unix line endings
# so the hashes will be stable with what's expected in our test cases.
if [[ "$OSTYPE" == "msys" ]]; then
    dos2unix --quiet "$TARGET_DIR/.npmrc"
fi

npm install --silent

git --git-dir="${TARGET_DIR}/.git" --work-tree="${TARGET_DIR}" add .
git --git-dir="${TARGET_DIR}/.git" --work-tree="${TARGET_DIR}" commit -m "Initial" --quiet
