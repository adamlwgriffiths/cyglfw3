"""Auto-generates bindings for GLFW.

Bindings are automatically created for both the .pxd and .pyx for:
   * #defines
   * structs
   * function pointers

Function bindings, callbacks and logic are not auto-generated and are provided by
a static block of code pre-pended to the .pyx file.

The regular expressions used in this file are dependent on
the GLFW coding style remaining consistent.
Changes to the GLFW coding style may break this code.
"""

import os
import re

cyglfw3_directory = os.path.join(os.path.dirname(__file__), '..', 'cyglfw3')

header_string = """
#
# This file is autogenerated.
# Changes should be made to 'generate_cython.py'.
# Re-run the script by running 'python generate_cython.py'
#
"""

define_regexp = re.compile(r'#define (?P<define>GLFW_[^\s]+)')
def defines(lines):
    for line in lines:
        match = define_regexp.search(line)
        if match:
            define = match.group('define')
            if 'DEFINED' in define:
                continue
            yield define


struct_regexp = re.compile(r'typedef struct (\w+)\s({(?P<variables>[^}]+)}\s)?(?P<name>\w+);', flags=re.DOTALL)
variable_regexp = re.compile(r'(?P<type>[\w\s\d\*]+)\s(?P<name>[\w\d]+)$', flags=re.DOTALL)
def structs(text):
    def extract_variables(text):
        # split by ;
        variables = text.split(';')

        for variable in variables:
            # strip and remove empty variables
            variable = variable.strip()
            if not len(variable):
                continue

            match = variable_regexp.search(variable)
            type = match.group('type')
            name = match.group('name')
            yield type, name

    for match in struct_regexp.finditer(text):
        name = match.group('name')
        variables = match.group('variables') or ''
        variables = list(extract_variables(variables))
        yield name, variables


void_regexp = re.compile(r'\(void\)')

fp_regexp = re.compile(r'typedef (?P<signature>void \(\*\s?\w+\)\([\w\d\s\*,]+\));')
def function_pointers(lines):
    for line in lines:
        match = fp_regexp.search(line)
        if match:
            signature = match.group('signature')
            signature = void_regexp.sub('()', signature)
            yield signature

function_regexp = re.compile(r'GLFWAPI (?P<return>[\w\s\d\*]+) (?P<name>[\w\d]+)\((?P<parameters>.*)\);')
def functions(lines):
    for line in lines:
        match = function_regexp.search(line)
        if match:
            ret = match.group('return')
            name = match.group('name')
            parameters = match.group('parameters')
            if 'void' == parameters:
                parameters = ''
            yield ret, name, parameters


header_paths = [
    # homebrew
    '/usr/local/include/GLFW/glfw3.h',
    # macports
    '/opt/local/include/GLFW/glfw3.h',
    # linux
    '/usr/include/GLFW/glfw3.h',
]

# windows
if 'GLFW_ROOT' in os.environ:
    header_paths.append(os.path.join(os.environ['GLFW_ROOT'], 'include/GLFW/glfw3.h'))

header = None
for path in header_paths:
    if os.path.exists(path):
        header = path
        break

if not header:
    raise ValueError('Unable to find GLFW header, please raise an issue at https://github.com/adamlwgriffiths/cyglfw3/issues')

strip_regexp = re.compile(r'/\*.*?\*/', flags=re.DOTALL)
with open(header, 'r') as f:
    text = f.read()
    text = strip_regexp.sub('', text)
    lines = text.split('\n')


pxd_supplemental = """
#
# Supplemental
#

"""


def generate_pxd():
    pxd_filename = os.path.join(cyglfw3_directory, 'cglfw3.pxd')
    pxd_lines = []

    pxd_lines += header_string.split('\n')

    pxd_lines.append('cdef extern from "GLFW/glfw3.h":')
    pxd_lines.append('\t')

    pxd_lines.append('\t#')
    pxd_lines.append('\t# Defines')
    pxd_lines.append('\t#')
    for define in defines(lines):
        pxd_lines.append('\tcdef int {define}'.format(define=define))
    pxd_lines.append('\t')

    pxd_lines.append('\t#')
    pxd_lines.append('\t# Structs')
    pxd_lines.append('\t#')
    for struct_name, variables in structs(text):
        pxd_lines.append('\tcdef struct {name}:'.format(name=struct_name))
        if len(variables):
            for variable_type, variable_name in variables:
                pxd_lines.append('\t\t{type} {name}'.format(type=variable_type, name=variable_name))
        else:
            pxd_lines.append('\t\tpass')
        pxd_lines.append('\t\t')
    pxd_lines.append('\t')

    pxd_lines.append('\t#')
    pxd_lines.append('\t# Function Pointers')
    pxd_lines.append('\t#')
    for fp in function_pointers(lines):
        pxd_lines.append('\tctypedef {signature}'.format(signature=fp))

    pxd_lines.append('\t')
    pxd_lines.append('\t#')
    pxd_lines.append('\t# Functions')
    pxd_lines.append('\t#')
    for ret, name, params in functions(lines):
        pxd_lines.append('\t{ret} {name}({params})'.format(ret=ret, name=name, params=params))
    pxd_lines.append('\t')

    pxd_lines += pxd_supplemental.split('\n')

    with open(pxd_filename, 'w') as f:
        pxd = '\n'.join(pxd_lines)
        pxd = pxd.replace('\t', '    ')
        f.write(pxd)



# this block is added to the bottom of the pyx file
# it should define the functions and classes
pyx_supplemental = """
#
# Supplemental
#

from libc.stdlib cimport malloc, free
from cython cimport view

#
# Callbacks
#

cdef object _error_fun
cdef void errorfun_cb(int a, const char* b):
    global _error_fun
    (<object>_error_fun)(a, b)

cdef dict _windowposfuns = {}
cdef void windowposfun_cb(cglfw3.GLFWwindow* a,int b,int c):
    cb = _windowposfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b, c)

cdef dict _windowsizefuns = {}
cdef void windowsizefun_cb(cglfw3.GLFWwindow* a,int b,int c):
    cb = _windowsizefuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b, c)

cdef dict _windowclosefuns = {}
cdef void windowclosefun_cb(cglfw3.GLFWwindow* a):
    cb = _windowclosefuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window)

cdef dict _windowrefreshfuns = {}
cdef void windowrefreshfun_cb(cglfw3.GLFWwindow* a):
    cb = _windowrefreshfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window)

cdef dict _windowfocusfuns = {}
cdef void windowfocusfun_cb(cglfw3.GLFWwindow* a,int b):
    cb = _windowfocusfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b)

cdef dict _windowiconifyfuns = {}
cdef void windowiconifyfun_cb(cglfw3.GLFWwindow* a,int b):
    cb = _windowiconifyfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b)

cdef dict _framebuffersizefuns = {}
cdef void framebuffersizefun_cb(cglfw3.GLFWwindow* a,int b,int c):
    cb = _framebuffersizefuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b, c)

cdef dict _mousebuttonfuns = {}
cdef void mousebuttonfun_cb(cglfw3.GLFWwindow* a,int b,int c,int d):
    cb = _mousebuttonfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b, c, d)

cdef dict _cursorposfuns = {}
cdef void cursorposfun_cb(cglfw3.GLFWwindow* a,double b,double c):
    cb = _cursorposfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b, c)

cdef dict _cursorenterfuns = {}
cdef void cursorenterfun_cb(cglfw3.GLFWwindow* a,int b):
    cb = _cursorenterfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b)

cdef dict _scrollfuns = {}
cdef void scrollfun_cb(cglfw3.GLFWwindow* a,double b,double c):
    cb = _scrollfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b, c)

cdef dict _keyfuns = {}
cdef void keyfun_cb(cglfw3.GLFWwindow* a,int b,int c,int d,int e):
    cb = _keyfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b, c, d, e)

cdef dict _charfuns = {}
cdef void charfun_cb(cglfw3.GLFWwindow* a,unsigned int b):
    cb = _charfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b)

cdef dict _charmodsfuns = {}
cdef void charmodsfun_cb(cglfw3.GLFWwindow* a,unsigned int b,int c):
    cb = _charmodsfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    cb(window, b, c)

cdef dict _dropfuns = {}
cdef void dropfun_cb(cglfw3.GLFWwindow* a,int b,const char** c):
    cb = _dropfuns[<size_t>a]
    window = Window()
    window._this_ptr = a
    d = [<bytes>c[i] for i in range(b)]
    cb(window, d)

cdef object _monitorfun
cdef void monitorfun_cb(cglfw3.GLFWmonitor* a,int b):
    global _monitorfun
    monitor = Monitor()
    monitor._this_ptr = a
    _monitorfun(monitor, b)

#
# Classes
#

cdef class Monitor:
    cdef const cglfw3.GLFWmonitor * _this_ptr
    
    def __cinit__(self):
        self._this_ptr = NULL

    def __richcmp__(Monitor self, Monitor other, int op):
        if op == 0:
            # <
            return self._this_ptr < other._this_ptr
        elif op == 1:
            # <=
            return self._this_ptr <= other._this_ptr
        elif op == 2:
            # ==
            return self._this_ptr == other._this_ptr
        elif op == 3:
            # !=
            return self._this_ptr != other._this_ptr
        elif op == 4:
            # >
            return self._this_ptr > other._this_ptr
        elif op == 5:
            # >=
            return self._this_ptr >= other._this_ptr
    
    def __hash__(self):
        return <size_t>self._this_ptr

cdef class Window:
    cdef const cglfw3.GLFWwindow * _this_ptr

    def __cinit__(self):
        self._this_ptr = NULL

    def __richcmp__(Window self, Window other, int op):
        if op == 0:
            # <
            return self._this_ptr < other._this_ptr
        elif op == 1:
            # <=
            return self._this_ptr <= other._this_ptr
        elif op == 2:
            # ==
            return self._this_ptr == other._this_ptr
        elif op == 3:
            # !=
            return self._this_ptr != other._this_ptr
        elif op == 4:
            # >
            return self._this_ptr > other._this_ptr
        elif op == 5:
            # >=
            return self._this_ptr >= other._this_ptr
    
    def __hash__(self):
        return <size_t>self._this_ptr

cdef class Cursor:
    cdef const cglfw3.GLFWcursor * _this_ptr
    
    def __cinit__(self):
        self._this_ptr = NULL

    def __richcmp__(Cursor self, Cursor other, int op):
        if op == 0:
            # <
            return self._this_ptr < other._this_ptr
        elif op == 1:
            # <=
            return self._this_ptr <= other._this_ptr
        elif op == 2:
            # ==
            return self._this_ptr == other._this_ptr
        elif op == 3:
            # !=
            return self._this_ptr != other._this_ptr
        elif op == 4:
            # >
            return self._this_ptr > other._this_ptr
        elif op == 5:
            # >=
            return self._this_ptr >= other._this_ptr
    
    def __hash__(self):
        return <size_t>self._this_ptr

cdef class VidMode:
    cdef const cglfw3.GLFWvidmode * _this_ptr
    def __cinit__(self):
        self._this_ptr = NULL

    property width:
        def __get__(self):
            return self._this_ptr.width

    property height:
        def __get__(self):
            return self._this_ptr.height

    property redBits:
        def __get__(self):
            return self._this_ptr.redBits

    property greenBits:
        def __get__(self):
            return self._this_ptr.greenBits

    property blueBits:
        def __get__(self):
            return self._this_ptr.blueBits

    property refreshRate:
        def __get__(self):
            return self._this_ptr.refreshRate

    def __richcmp__(VidMode self, VidMode other, int op):
        us = (self.width, self.height, self.redBits, self.greenBits, self.blueBits, self.refreshRate)
        them = (other.width, other.height, other.redBits, other.greenBits, other.blueBits, other.refreshRate)
        if op == 0:
            # <
            return us < them
        elif op == 1:
            # <=
            return us <= them
        elif op == 2:
            # ==
            return us == them
        elif op == 3:
            # !=
            return us != them
        elif op == 4:
            # >
            return us > them
        elif op == 5:
            # >=
            return us >= them
    
    def __hash__(self):
        return <size_t>self._this_ptr

cdef class GammaRamp:
    cdef const cglfw3.GLFWgammaramp * _this_ptr
    def __cinit__(self):
        self._this_ptr = NULL

    property red:
        def __get__(self):
            red = [] * self._this_ptr.size

            for i in range(self._this_ptr.size):
                red[i] = self._this_ptr.red[i]
            return red

    property green:
        def __get__(self):
            green = [] * self._this_ptr.size

            for i in range(self._this_ptr.size):
                green[i] = self._this_ptr.green[i]
            return green

    property blue:
        def __get__(self):
            blue = [] * self._this_ptr.size

            for i in range(self._this_ptr.size):
                blue[i] = self._this_ptr.blue[i]
            return blue

    def __richcmp__(GammaRamp self, GammaRamp other, int op):
        us = (self.red, self.green, self.blue)
        them = (other.red, other.green, other.blue)
        if op == 0:
            # <
            return us < them
        elif op == 1:
            # <=
            return us <= them
        elif op == 2:
            # ==
            return us == them
        elif op == 3:
            # !=
            return us != them
        elif op == 4:
            # >
            return us > them
        elif op == 5:
            # >=
            return us >= them
    
    def __hash__(self):
        return <size_t>self._this_ptr

cdef getitem(obj, key, default=None):
    try:
        return obj[key]
    except (TypeError, KeyError, IndexError):
        return default

cdef getlen(obj, default=None):
    try:
        return len(obj)
    except TypeError:
        return default

cdef getshape(obj):
    lengths = []
    while True:
        length, obj = getlen(obj), getitem(obj, 0)
        if length is None: break
        lengths.append(length)
    return tuple(lengths)

cdef class Image:
    cdef cglfw3.GLFWimage * _this_ptr
    cdef unsigned char[:,:,::1] _data

    property width:
        def __get__(self):
            return self._this_ptr.width

    property height:
        def __get__(self):
            return self._this_ptr.height

    property size:
        def __get__(self):
            return (self.width, self.height)

    property pixels:
        def __get__(self):
            return self._data

        def __set__(self, value):
            cdef unsigned char[:,:,::1] data
            if isinstance(value, (tuple, list)):
                shape = getshape(value)
                data = view.array(shape=(shape[0], shape[1], 4), itemsize=sizeof(unsigned char), format="c")
                for i in range(shape[0]):
                    for j in range(shape[1]):
                        data[i,j,0] = getitem(value[i][j], 0, 0x00)
                        data[i,j,1] = getitem(value[i][j], 1, 0x00)
                        data[i,j,2] = getitem(value[i][j], 2, 0x00)
                        data[i,j,3] = getitem(value[i][j], 3, 0xFF)
            else:
                # must be a (writable) memory view or a buffer type
                data = value

            self._this_ptr.width = data.shape[0]
            self._this_ptr.height = data.shape[1]
            self._this_ptr.pixels = &data[0][0][0]

            self._data = data

    def __cinit__(self):
        self._this_ptr = NULL

    def __init__(self, pixels=None):
        self._this_ptr = <cglfw3.GLFWimage *>malloc(sizeof(cglfw3.GLFWimage))
        
        if pixels is not None:
            self.pixels = pixels
        
    def __dealloc__(self):
        free(self._this_ptr)
        self._this_ptr = NULL

    def __richcmp__(Image self, Image other, int op):
        if op == 0:
            # <
            return self._this_ptr < other._this_ptr
        elif op == 1:
            # <=
            return self._this_ptr <= other._this_ptr
        elif op == 2:
            # ==
            return self._this_ptr == other._this_ptr
        elif op == 3:
            # !=
            return self._this_ptr != other._this_ptr
        elif op == 4:
            # >
            return self._this_ptr > other._this_ptr
        elif op == 5:
            # >=
            return self._this_ptr >= other._this_ptr
    
    def __nonzero__(self):
        return self._this_ptr != NULL
    
    def __hash__(self):
        return <size_t>self._this_ptr

#
# Functions
#
def Init():
    return cglfw3.glfwInit()

def Terminate():
    cglfw3.glfwTerminate()

def GetVersion():
    cdef int major, minor, rev
    cglfw3.glfwGetVersion(&major, &minor, &rev)
    return major, minor, rev

def GetVersionString():
    return cglfw3.glfwGetVersionString()

def SetErrorCallback(cbfun):
    global _error_fun
    _error_fun = cbfun
    cglfw3.glfwSetErrorCallback(errorfun_cb)

def GetMonitors():
    cdef int count
    cdef cglfw3.GLFWmonitor ** c_monitors = NULL
    c_monitors = cglfw3.glfwGetMonitors(&count)

    monitors = []
    for i in range(count):
        monitor = Monitor()
        monitor._this_ptr = c_monitors[i]
        monitors.append(monitor)
    return monitors

def GetPrimaryMonitor():
    cdef const cglfw3.GLFWmonitor* c_monitor = cglfw3.glfwGetPrimaryMonitor()
    monitor = Monitor()
    monitor._this_ptr = c_monitor
    return monitor

def GetMonitorPos(Monitor monitor):
    cdef int x, y
    cglfw3.glfwGetMonitorPos(<cglfw3.GLFWmonitor*>monitor._this_ptr, &x, &y)
    return x, y

def GetMonitorPhysicalSize(Monitor monitor):
    cdef int width, height
    cglfw3.glfwGetMonitorPhysicalSize(<cglfw3.GLFWmonitor*>monitor._this_ptr, &width, &height)
    return width, height

def GetMonitorName(Monitor monitor):
    return cglfw3.glfwGetMonitorName(<cglfw3.GLFWmonitor*>monitor._this_ptr)

def SetMonitorCallback(cbfun):
    global _monitorfun
    _monitorfun = cbfun
    cglfw3.glfwSetMonitorCallback(monitorfun_cb)

def GetVideoModes(Monitor monitor):
    cdef int count
    cdef const cglfw3.GLFWvidmode* c_vidmodes = cglfw3.glfwGetVideoModes(<cglfw3.GLFWmonitor*>monitor._this_ptr, &count)

    vidmodes = []
    for i in range(count):
        vidmode = VidMode()
        vidmode._this_ptr = &c_vidmodes[i]
        vidmodes.append(vidmode)
    return vidmodes

def GetVideoMode(Monitor monitor):
    cdef const cglfw3.GLFWvidmode* c_vidmode = cglfw3.glfwGetVideoMode(<cglfw3.GLFWmonitor*>monitor._this_ptr)
    vidmode = VidMode()
    vidmode._this_ptr = c_vidmode
    return vidmode

def SetGamma(Monitor monitor, float gamma):
    cglfw3.glfwSetGamma(<cglfw3.GLFWmonitor*>monitor._this_ptr, gamma)

def GetGammaRamp(Monitor monitor):
    cdef const cglfw3.GLFWgammaramp* c_gammaramp = cglfw3.glfwGetGammaRamp(<cglfw3.GLFWmonitor*>monitor._this_ptr)
    gammaramp = GammaRamp()
    gammaramp._this_ptr = c_gammaramp
    return gammaramp

def DefaultWindowHints():
    cglfw3.glfwDefaultWindowHints()

def WindowHint(int target, int hint):
    cglfw3.glfwWindowHint(target, hint)

def CreateWindow(int width, int height, char* title, Monitor monitor=None, Window window=None):
    cdef cglfw3.GLFWmonitor* glfwmonitor = NULL
    cdef cglfw3.GLFWwindow* glfwwindow = NULL
    if monitor:
        glfwmonitor = <cglfw3.GLFWmonitor*>monitor._this_ptr
    if window:
        glfwwindow = <cglfw3.GLFWwindow*>window._this_ptr

    cdef const cglfw3.GLFWwindow* c_window = cglfw3.glfwCreateWindow(width, height, title, glfwmonitor, glfwwindow)
    window_ = Window()
    window_._this_ptr = c_window
    return window_

def DestroyWindow(Window window):
    cglfw3.glfwDestroyWindow(<cglfw3.GLFWwindow*>window._this_ptr)

def WindowShouldClose(Window window):
    return cglfw3.glfwWindowShouldClose(<cglfw3.GLFWwindow*>window._this_ptr)

def SetWindowShouldClose(Window window, int value):
    cglfw3.glfwSetWindowShouldClose(<cglfw3.GLFWwindow*>window._this_ptr, value)

def SetWindowTitle(Window window, const char* title):
    cglfw3.glfwSetWindowTitle(<cglfw3.GLFWwindow*>window._this_ptr, title)

def GetWindowPos(Window window):
    cdef int x, y
    cglfw3.glfwGetWindowPos(<cglfw3.GLFWwindow*>window._this_ptr, &x, &y)
    return x, y

def SetWindowPos(Window window, int xpos, int ypos):
    cglfw3.glfwSetWindowPos(<cglfw3.GLFWwindow*>window._this_ptr, xpos, ypos)

def GetWindowSize(Window window):
    cdef int width, height
    cglfw3.glfwGetWindowSize(<cglfw3.GLFWwindow*>window._this_ptr, &width, &height)
    return width, height

def SetWindowSize(Window window, int width, int height):
    cglfw3.glfwSetWindowSize(<cglfw3.GLFWwindow*>window._this_ptr, width, height)

def GetFramebufferSize(Window window):
    cdef int width, height
    cglfw3.glfwGetFramebufferSize(<cglfw3.GLFWwindow*>window._this_ptr, &width, &height)
    return width, height

def GetWindowFrameSize(Window window):
    cdef int left, top, right, bottom
    cglfw3.glfwGetWindowFrameSize(<cglfw3.GLFWwindow*>window._this_ptr, &left, &top, &right, &bottom)
    return left, top, right, bottom

def IconifyWindow(Window window):
    cglfw3.glfwIconifyWindow(<cglfw3.GLFWwindow*>window._this_ptr)

def RestoreWindow(Window window):
    cglfw3.glfwRestoreWindow(<cglfw3.GLFWwindow*>window._this_ptr)

def ShowWindow(Window window):
    cglfw3.glfwShowWindow(<cglfw3.GLFWwindow*>window._this_ptr)

def HideWindow(Window window):
    cglfw3.glfwHideWindow(<cglfw3.GLFWwindow*>window._this_ptr)

def GetWindowAttrib(Window window, int attrib):
    return cglfw3.glfwGetWindowAttrib(<cglfw3.GLFWwindow*>window._this_ptr, attrib)

#def SetWindowUserPointer(Window window, void* pointer):
#    pass
#
#def GetWindowUserPointer(Window window):
#    pass

def SetWindowPosCallback(Window window, cbfun):
    global _windowposfuns
    _windowposfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetWindowPosCallback(<cglfw3.GLFWwindow*>window._this_ptr, windowposfun_cb)

def SetWindowSizeCallback(Window window, cbfun):
    global _windowsizefuns
    _windowsizefuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetWindowSizeCallback(<cglfw3.GLFWwindow*>window._this_ptr, windowsizefun_cb)

def SetWindowCloseCallback(Window window, cbfun):
    global _windowclosefuns
    _windowclosefuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetWindowCloseCallback(<cglfw3.GLFWwindow*>window._this_ptr, windowclosefun_cb)

def SetWindowRefreshCallback(Window window, cbfun):
    global _windowrefreshfuns
    _windowrefreshfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetWindowRefreshCallback(<cglfw3.GLFWwindow*>window._this_ptr, windowrefreshfun_cb)

def SetWindowFocusCallback(Window window, cbfun):
    global _windowfocusfuns
    _windowfocusfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetWindowFocusCallback(<cglfw3.GLFWwindow*>window._this_ptr, windowfocusfun_cb)

def SetWindowIconifyCallback(Window window, cbfun):
    global _windowiconifyfuns
    _windowiconifyfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetWindowIconifyCallback(<cglfw3.GLFWwindow*>window._this_ptr, windowiconifyfun_cb)

def SetFramebufferSizeCallback(Window window, cbfun):
    global _framebuffersize
    _framebuffersizefuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetFramebufferSizeCallback(<cglfw3.GLFWwindow*>window._this_ptr, framebuffersizefun_cb)

def PollEvents():
    cglfw3.glfwPollEvents()

def WaitEvents():
    cglfw3.glfwWaitEvents()

def PostEmptyEvent():
    cglfw3.glfwPostEmptyEvent()

def GetInputMode(Window window, int mode):
    return cglfw3.glfwGetInputMode(<cglfw3.GLFWwindow*>window._this_ptr, mode)

def SetInputMode(Window window, int mode, int value):
    cglfw3.glfwSetInputMode(<cglfw3.GLFWwindow*>window._this_ptr, mode, value)

def GetKey(Window window, int key):
    return cglfw3.glfwGetKey(<cglfw3.GLFWwindow*>window._this_ptr, key)

def GetMouseButton(Window window, int button):
    return cglfw3.glfwGetMouseButton(<cglfw3.GLFWwindow*>window._this_ptr, button)

def GetCursorPos(Window window):
    cdef double x, y
    cglfw3.glfwGetCursorPos(<cglfw3.GLFWwindow*>window._this_ptr, &x, &y)
    return x, y

def SetCursorPos(Window window, double xpos, double ypos):
    cglfw3.glfwSetCursorPos(<cglfw3.GLFWwindow*>window._this_ptr, xpos, ypos)

def CreateCursor(Image image, int xhot, int yhot):
    cdef const cglfw3.GLFWcursor* c_cursor = cglfw3.glfwCreateCursor(<cglfw3.GLFWimage*>image._this_ptr, xhot, yhot)
    
    cursor = Cursor()
    cursor._this_ptr = c_cursor
    return cursor

def CreateStandardCursor(int shape):
    cdef const cglfw3.GLFWcursor* c_cursor = cglfw3.glfwCreateStandardCursor(shape)
    
    cursor = Cursor()
    cursor._this_ptr = c_cursor
    return cursor

def DestroyCursor(Cursor cursor):
    cglfw3.glfwDestroyCursor(<cglfw3.GLFWcursor*>cursor._this_ptr)

def SetCursor(Window window, Cursor cursor):
    cglfw3.glfwSetCursor(<cglfw3.GLFWwindow*>window._this_ptr, <cglfw3.GLFWcursor*>cursor._this_ptr)

def SetKeyCallback(Window window, cbfun):
    global _keyfuns
    _keyfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetKeyCallback(<cglfw3.GLFWwindow*>window._this_ptr, keyfun_cb)

def SetCharCallback(Window window, cbfun):
    global _charfuns
    _charfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetCharCallback(<cglfw3.GLFWwindow*>window._this_ptr, charfun_cb)

def SetCharModsCallback(Window window, cbfun):
    global _charmodsfuns
    _charmodsfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetCharModsCallback(<cglfw3.GLFWwindow*>window._this_ptr, charmodsfun_cb)

def SetMouseButtonCallback(Window window, cbfun):
    global _mousebuttonfuns
    _mousebuttonfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetMouseButtonCallback(<cglfw3.GLFWwindow*>window._this_ptr, mousebuttonfun_cb)

def SetCursorPosCallback(Window window, cbfun):
    global _cursorposfuns
    _cursorposfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetCursorPosCallback(<cglfw3.GLFWwindow*>window._this_ptr, cursorposfun_cb)

def SetCursorEnterCallback(Window window, cbfun):
    global _cursorenterfuns
    _cursorenterfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetCursorEnterCallback(<cglfw3.GLFWwindow*>window._this_ptr, cursorenterfun_cb)

def SetScrollCallback(Window window, cbfun):
    global _scrollfuns
    _scrollfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetScrollCallback(<cglfw3.GLFWwindow*>window._this_ptr, scrollfun_cb)

def SetDropCallback(Window window, cbfun):
    global _dropfuns
    _dropfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetDropCallback(<cglfw3.GLFWwindow*>window._this_ptr, dropfun_cb)

def JoystickPresent(int joy):
    return cglfw3.glfwJoystickPresent(joy)

def GetJoystickAxes(int joy):
    cdef int count
    cdef const float* c_axes = cglfw3.glfwGetJoystickAxes(joy, &count)
    axes = [
        float(c_axes[i])
        for i in range(count)
    ]
    return axes

def GetJoystickButtons(int joy):
    cdef int count
    cdef const unsigned char* c_buttons = cglfw3.glfwGetJoystickButtons(joy, &count)
    buttons = [
        int(c_buttons[i])
        for i in range(count)
    ]
    return buttons

def GetJoystickName(int joy):
    return str(cglfw3.glfwGetJoystickName(joy))

def SetClipboardString(Window window, const char* string):
    cglfw3.glfwSetClipboardString(<cglfw3.GLFWwindow*>window._this_ptr, string)

def GetClipboardString(Window window):
    return str(cglfw3.glfwGetClipboardString(<cglfw3.GLFWwindow*>window._this_ptr))

def GetTime():
    return cglfw3.glfwGetTime()

def SetTime(double time):
    cglfw3.glfwSetTime(time)

def MakeContextCurrent(Window window):
    cglfw3.glfwMakeContextCurrent(<cglfw3.GLFWwindow*>window._this_ptr)

def GetCurrentContext():
    cdef const cglfw3.GLFWwindow * c_window = cglfw3.glfwGetCurrentContext()
    if not c_window:
        return None

    window = Window()
    window._this_ptr = c_window
    return window

def SwapBuffers(Window window):
    cglfw3.glfwSwapBuffers(<cglfw3.GLFWwindow*>window._this_ptr)

def SwapInterval(int interval):
    cglfw3.glfwSwapInterval(interval)

def ExtensionSupported(const char* extension):
    return cglfw3.glfwExtensionSupported(extension)

def GetProcAddress(const char* procname):
    return <size_t>cglfw3.glfwGetProcAddress(procname)

"""


strip_define_regexp = re.compile(r'GLFW_')
strip_function_regexp = re.compile(r'glfw')

def generate_pyx():
    pyx_filename = os.path.join(cyglfw3_directory, 'glfw3.pyx')
    pyx_lines = []

    pyx_lines += header_string.split('\n')

    pyx_lines.append('cimport cyglfw3.cglfw3 as cglfw3')
    pyx_lines.append('')

    pyx_lines.append('#')
    pyx_lines.append('# Defines')
    pyx_lines.append('#')
    for define in defines(lines):
        variable = strip_define_regexp.sub('', define)
        pyx_lines.append('{variable} = cglfw3.{define}'.format(variable=variable, define=define))
    pyx_lines.append('\t')

    pyx_lines += pyx_supplemental.split('\n')

    with open(pyx_filename, 'w') as f:
        pyx = '\n'.join(pyx_lines)
        pyx = pyx.replace('\t', '    ')
        f.write(pyx)


generate_pxd()
generate_pyx()
