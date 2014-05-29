import sys
from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext
from Cython.Build import cythonize
"""
# auto-install cython
from setuptools.dist import Distribution
Distribution(dict(setup_requires='Cython'))

# check cython is installed
try:
    from Cython.Distutils import build_ext
except ImportError:
    print("Could not import Cython.Distutils. Install `cython` and rerun.")
    sys.exit(1)
"""
# set the GLFW compiler flags
extra_compile_args = []
extra_link_args = []
if 'darwin' in sys.platform:
    # check for homebrew
    extra_compile_args.append('-I/usr/local/include')
    extra_link_args.append('-L/usr/local/lib')

ext_modules = [
    Extension('cyglfw3.glfw3', ['cyglfw3/glfw3.pyx'], libraries=['glfw3'],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args
    )
]
ext_modules = cythonize(ext_modules)

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
)
