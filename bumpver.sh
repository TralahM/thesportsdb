#!/usr/bin/env bash

usage() {
  echo "Bump version"
  echo "Usage: "
  echo "$0 <new version>"
  echo
  echo "example: $0 0.3.5"
}

if [ $# -lt 1 ]; then
  usage
  exit 1
fi

VER="$1"
STAGE=0
echo "bumping to $VER"

sed -i "s/^\(version.*=.*\) \([0-9].*\)/\1 $VER/g" setup.cfg
sed -i "s/^\(__version__.*=.*\"\)\([0-9].*\)\"/\1$VER\"/g" thesportsdb/__init__.py

shift

for arg in "$@"; do
  case $arg in
    -s|--stage)
      echo "staging"
      git add setup.cfg thesportsdb/__init__.py
      git commit -m "chore: bump v$VER"|| true
      ;;
    -c|--chlog)
      echo "changelog"
      git stash push CHANGELOG.md;
      git cliff -o CHANGELOG.md --bump --tag "$VER"
      git stash clear
      git add CHANGELOG.md
      git commit -m "changelog" || true
      ;;
  esac
done
