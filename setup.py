import sys
from setuptools import setup, Extension
from setuptools.dist import Distribution

requires = ['Cython']
packages = ['cyglfw3']

# auto-install cython
Distribution(dict(setup_requires='Cython'))

# check cython is installed
try:
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize
except ImportError:
    print("Could not import Cython. Install `cython` and rerun.")
    sys.exit(1)

# set the GLFW compiler flags
extra_compile_args = []
extra_link_args = []

platform = sys.platform.lower()
if 'darwin' in platform or 'linux' in platform:
    # check for homebrew or local installations on unix systems
    extra_compile_args.append('-I/usr/local/include')
    extra_link_args.append('-L/usr/local/lib')

glfw_lib = 'glfw'
if 'darwin' in platform:
    # homebrew calls it libglfw3
    glwf_lib = 'glfw3'

ext_modules = [
    Extension('cyglfw3.glfw3', 
        ['cyglfw3/glfw3.pyx'], 
        libraries=[glwf_lib],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args
    )
]
ext_modules = cythonize(ext_modules)

setup_dict = dict(
    name="cyglfw3",
    version='0.0.1',
    description="Python bindings for GLFW 3+ using Cython",
    author="Adam Griffiths",
    author_email="adam.lw.griffiths@gmail.com",
    install_requires=requires,
    url='http://github.com/adamlwgriffiths/cyglfw3',
    packages=packages,
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
    classifiers=(
        'Development Status :: 2 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: ??',
        'Programming Language :: Python',
    ),
)

setup(**setup_dict)