#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd $DIR

cd ..

# delete old
rm cyglfw3/glfw3.{c,so,pyx,}
rm cyglfw3/cglfw3.{pxd,}

# generate bindings
python scripts/generate_cython.py

# build lib
python setup.py build_ext -i

popd
