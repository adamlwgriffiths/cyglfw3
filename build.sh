#!/bin/bash
set -e

clear
rm -rf *.{so,c} build cyglfw3/*.{so,c}
python generate_cython.py
python setup.py build_ext -i
#python -m unittest discover tests
