#!/usr/bin/env bash

dd=$(mktemp -d -t prysk-tests-)
echo "Using temporary directory: $dd"

pushd "$dd" || exit 1

git init --quiet --initial-branch=main
touch foo

ls -al "$dd"
ls -al "$dd/.git"

git --git-dir="$dd/.git" --work-tree="$dd" config user.email "turbo-test@example.com"
git --git-dir="$dd/.git" --work-tree="$dd" config user.name "Turbo Test"

git --git-dir="$dd/.git" --work-tree="$dd" add .
git --git-dir="$dd/.git" --work-tree="$dd" commit -m "Initial" --quiet


echo "Deleting temporary directory: $dd"
rm -rf "$dd"

popd || exit 1
