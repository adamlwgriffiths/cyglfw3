import os
import sys
from setuptools import setup, Extension
from setuptools.dist import Distribution

with open("./cyglfw3/version.py") as versionfile:
    exec(versionfile.read())

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

    # support macports
    extra_compile_args.append('-I/opt/local/include')
    extra_compile_args.append('-I/opt/local/lib')

glfw_lib = 'glfw'
if 'darwin' in platform:
    # homebrew calls it libglfw3
    if os.path.exists('/usr/local/lib/libglfw3.dylib'):
        glfw_lib = 'glfw3'

if 'win32' in platform:
    glfw_lib = 'glfw3dll'
    if 'GLFW_ROOT' in os.environ:
        extra_compile_args.append('-I%s' % (os.path.join(os.environ['GLFW_ROOT'], 'include'),))
        extra_link_args.append('/LIBPATH:%s' % (os.path.join(os.environ['GLFW_ROOT'], 'lib-vc2012'),))

ext_modules = [
    Extension('cyglfw3.glfw3', ['cyglfw3/glfw3.pyx'], libraries=[glfw_lib],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args
    )
]
ext_modules = cythonize(ext_modules)

# import the README
with open('README.rst') as f:
    long_description = f.read()


setup(
    name="cyglfw3",
    version=__version__,
    description="Python bindings for GLFW 3+ using Cython",
    long_description=long_description,
    license = 'BSD',
    author="Adam Griffiths",
    install_requires=['Cython'],
    url='http://github.com/adamlwgriffiths/cyglfw3',
    packages=['cyglfw3'],
    package_data={'cyglfw3':['*.pyx', '*.pxd', '*.c']},
    cmdclass={'build_ext': build_ext},
    requires=['cython'],
    ext_modules=ext_modules,
    platforms=['any'],
    classifiers=(
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
