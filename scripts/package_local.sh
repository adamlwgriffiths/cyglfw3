#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pushd $DIR

cd ..
#EXISTING=`pip list | grep cyglfw3 | sed -e 's/cyglfw3 (//' | sed -e 's/,.*//'`
#EXISTING=`pip list | grep cyglfw3 | sed -n 's/cyglfw3 \(([^\)\.0-9]+)/\1/'`
#echo $EXISTING
#pip uninstall -y "dist/cyglfw3-$EXISTING.tar.gz"
# this isn't working for some reason
# so we have to use install --upgrade later
pip uninstall cyglfw3

python setup.py sdist

# get the latest version
# this script will fail if the version numbers aren't sortable
LATEST=`ls dist/cyglfw3-*.tar.gz | sort -nr | head -n 1`
pip install --upgrade --force-reinstall $LATEST

popd
