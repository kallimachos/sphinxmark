#!/bin/bash
# coding: utf-8

# Helper script for publishing documentation to a gh-page branch.
# Run from the master branch of the repository to publish.

# set current directory
STARTDIR=`pwd`

# set repo root directory
GITDIR=`git rev-parse --show-toplevel`

# set source directories
DOC='doc'
SOURCE='source'
CONFIG='tox.ini'

# ensure master is up-to-date
cd $GITDIR
BASEDIR=${PWD##*/}
git pull

# checkout gh-pages branch and delete contents except . files
git checkout gh-pages
find * -not -name ".*" -delete

# checkout source directories from master and reset HEAD
git checkout master $DOC $SOURCE $CONFIG
git reset HEAD

# build html from rst in internal directory
cd $DOC
make html

# move html files to root directory
mv -fv _build/html/* $GITDIR/

# remove source files
cd $GITDIR
rm -rf $DOC $SOURCE $CONFIG

# add, commit, and push new html files
git add .
git commit -m "gh-pages: `git log master -1 --pretty=short --abbrev-commit`"
git push origin gh-pages

# checkout master and signal completion
git checkout master
cd $STARTDIR
echo
if test `tput -T $TERM colors` -lt 256; then
    echo "Docs published to http://kallimachos.github.io/$BASEDIR"
else
    tput -T $TERM setaf 2
    echo "Docs published to http://kallimachos.github.io/$BASEDIR"
    tput -T $TERM sgr0
fi
