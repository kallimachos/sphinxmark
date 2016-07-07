#!/bin/bash

if [ "$TRAVIS_REPO_SLUG" == "kallimachos/sphinx-watermark" ] && \
    [ "$TRAVIS_PULL_REQUEST" == "false" ] && \
    [ "$TRAVIS_BRANCH" == "master" ]; then

    echo -e "Publishing gh-pages...\n"

    cp -r doc/_build/html $HOME

    cd $HOME
    git config --global user.email "travis@travis-ci.org"
    git config --global user.name "travis-ci"
    git clone --quiet \
        --branch=gh-pages \
        https://$GH_TOKEN@github.com/kallimachos/sphinx-watermark \
        gh-pages > /dev/null

    cd gh-pages
    find * -not -name ".*" -delete
    cp -rv $HOME/html/* ./
    git add -A .
    git commit -m "Latest doc on successful travis build $TRAVIS_BUILD_NUMBER\
    auto-pushed to gh-pages"
    git push -fq origin gh-pages > /dev/null

    if test `tput -T $TERM colors` -lt 256; then
        echo "Docs published to http://kallimachos.github.io/sphinx-watermark"
    else
        tput -T $TERM setaf 2
        echo "Docs published to http://kallimachos.github.io/sphinx-watermark"
        tput -T $TERM sgr0
    fi

    else
        echo -e "Not a merge to master. Not deploying to gh-pages."
fi
