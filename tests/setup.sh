#!/usr/bin/env bash

TARGET_DIR=$1

# TMPDIR=$(mktemp -d) # TODO: is this the issue?
THIS_DIR=$(dirname "${BASH_SOURCE[0]}")
cp -a "${THIS_DIR}/fixture/." "${TARGET_DIR}/"
git init "${TARGET_DIR}" --quiet --initial-branch=main
if [[ "$OSTYPE" == "msys" ]]; then $ git config --local core.autocrlf true; fi
git --git-dir="${TARGET_DIR}/.git" --work-tree="${TARGET_DIR}" config user.email "turbo-test@example.com"
git --git-dir="${TARGET_DIR}/.git" --work-tree="${TARGET_DIR}" config user.name "Turbo Test"
echo "script-shell=$(which bash)" > ${TARGET_DIR}/.npmrc
npm install --silent
git --git-dir="${TARGET_DIR}/.git" --work-tree="${TARGET_DIR}" add .
git --git-dir="${TARGET_DIR}/.git" --work-tree="${TARGET_DIR}" commit -m "Initial" --quiet
