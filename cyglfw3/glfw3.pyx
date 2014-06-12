
#
# This file is autogenerated.
# Changes should be made to 'generate_cython.py'.
# Re-run the script by running 'python generate_cython.py'
#

cimport cyglfw3.cglfw3 as cglfw3

#
# Defines
#
VERSION_MAJOR = cglfw3.GLFW_VERSION_MAJOR
VERSION_MINOR = cglfw3.GLFW_VERSION_MINOR
VERSION_REVISION = cglfw3.GLFW_VERSION_REVISION
RELEASE = cglfw3.GLFW_RELEASE
PRESS = cglfw3.GLFW_PRESS
REPEAT = cglfw3.GLFW_REPEAT
KEY_UNKNOWN = cglfw3.GLFW_KEY_UNKNOWN
KEY_SPACE = cglfw3.GLFW_KEY_SPACE
KEY_APOSTROPHE = cglfw3.GLFW_KEY_APOSTROPHE
KEY_COMMA = cglfw3.GLFW_KEY_COMMA
KEY_MINUS = cglfw3.GLFW_KEY_MINUS
KEY_PERIOD = cglfw3.GLFW_KEY_PERIOD
KEY_SLASH = cglfw3.GLFW_KEY_SLASH
KEY_0 = cglfw3.GLFW_KEY_0
KEY_1 = cglfw3.GLFW_KEY_1
KEY_2 = cglfw3.GLFW_KEY_2
KEY_3 = cglfw3.GLFW_KEY_3
KEY_4 = cglfw3.GLFW_KEY_4
KEY_5 = cglfw3.GLFW_KEY_5
KEY_6 = cglfw3.GLFW_KEY_6
KEY_7 = cglfw3.GLFW_KEY_7
KEY_8 = cglfw3.GLFW_KEY_8
KEY_9 = cglfw3.GLFW_KEY_9
KEY_SEMICOLON = cglfw3.GLFW_KEY_SEMICOLON
KEY_EQUAL = cglfw3.GLFW_KEY_EQUAL
KEY_A = cglfw3.GLFW_KEY_A
KEY_B = cglfw3.GLFW_KEY_B
KEY_C = cglfw3.GLFW_KEY_C
KEY_D = cglfw3.GLFW_KEY_D
KEY_E = cglfw3.GLFW_KEY_E
KEY_F = cglfw3.GLFW_KEY_F
KEY_G = cglfw3.GLFW_KEY_G
KEY_H = cglfw3.GLFW_KEY_H
KEY_I = cglfw3.GLFW_KEY_I
KEY_J = cglfw3.GLFW_KEY_J
KEY_K = cglfw3.GLFW_KEY_K
KEY_L = cglfw3.GLFW_KEY_L
KEY_M = cglfw3.GLFW_KEY_M
KEY_N = cglfw3.GLFW_KEY_N
KEY_O = cglfw3.GLFW_KEY_O
KEY_P = cglfw3.GLFW_KEY_P
KEY_Q = cglfw3.GLFW_KEY_Q
KEY_R = cglfw3.GLFW_KEY_R
KEY_S = cglfw3.GLFW_KEY_S
KEY_T = cglfw3.GLFW_KEY_T
KEY_U = cglfw3.GLFW_KEY_U
KEY_V = cglfw3.GLFW_KEY_V
KEY_W = cglfw3.GLFW_KEY_W
KEY_X = cglfw3.GLFW_KEY_X
KEY_Y = cglfw3.GLFW_KEY_Y
KEY_Z = cglfw3.GLFW_KEY_Z
KEY_LEFT_BRACKET = cglfw3.GLFW_KEY_LEFT_BRACKET
KEY_BACKSLASH = cglfw3.GLFW_KEY_BACKSLASH
KEY_RIGHT_BRACKET = cglfw3.GLFW_KEY_RIGHT_BRACKET
KEY_GRAVE_ACCENT = cglfw3.GLFW_KEY_GRAVE_ACCENT
KEY_WORLD_1 = cglfw3.GLFW_KEY_WORLD_1
KEY_WORLD_2 = cglfw3.GLFW_KEY_WORLD_2
KEY_ESCAPE = cglfw3.GLFW_KEY_ESCAPE
KEY_ENTER = cglfw3.GLFW_KEY_ENTER
KEY_TAB = cglfw3.GLFW_KEY_TAB
KEY_BACKSPACE = cglfw3.GLFW_KEY_BACKSPACE
KEY_INSERT = cglfw3.GLFW_KEY_INSERT
KEY_DELETE = cglfw3.GLFW_KEY_DELETE
KEY_RIGHT = cglfw3.GLFW_KEY_RIGHT
KEY_LEFT = cglfw3.GLFW_KEY_LEFT
KEY_DOWN = cglfw3.GLFW_KEY_DOWN
KEY_UP = cglfw3.GLFW_KEY_UP
KEY_PAGE_UP = cglfw3.GLFW_KEY_PAGE_UP
KEY_PAGE_DOWN = cglfw3.GLFW_KEY_PAGE_DOWN
KEY_HOME = cglfw3.GLFW_KEY_HOME
KEY_END = cglfw3.GLFW_KEY_END
KEY_CAPS_LOCK = cglfw3.GLFW_KEY_CAPS_LOCK
KEY_SCROLL_LOCK = cglfw3.GLFW_KEY_SCROLL_LOCK
KEY_NUM_LOCK = cglfw3.GLFW_KEY_NUM_LOCK
KEY_PRINT_SCREEN = cglfw3.GLFW_KEY_PRINT_SCREEN
KEY_PAUSE = cglfw3.GLFW_KEY_PAUSE
KEY_F1 = cglfw3.GLFW_KEY_F1
KEY_F2 = cglfw3.GLFW_KEY_F2
KEY_F3 = cglfw3.GLFW_KEY_F3
KEY_F4 = cglfw3.GLFW_KEY_F4
KEY_F5 = cglfw3.GLFW_KEY_F5
KEY_F6 = cglfw3.GLFW_KEY_F6
KEY_F7 = cglfw3.GLFW_KEY_F7
KEY_F8 = cglfw3.GLFW_KEY_F8
KEY_F9 = cglfw3.GLFW_KEY_F9
KEY_F10 = cglfw3.GLFW_KEY_F10
KEY_F11 = cglfw3.GLFW_KEY_F11
KEY_F12 = cglfw3.GLFW_KEY_F12
KEY_F13 = cglfw3.GLFW_KEY_F13
KEY_F14 = cglfw3.GLFW_KEY_F14
KEY_F15 = cglfw3.GLFW_KEY_F15
KEY_F16 = cglfw3.GLFW_KEY_F16
KEY_F17 = cglfw3.GLFW_KEY_F17
KEY_F18 = cglfw3.GLFW_KEY_F18
KEY_F19 = cglfw3.GLFW_KEY_F19
KEY_F20 = cglfw3.GLFW_KEY_F20
KEY_F21 = cglfw3.GLFW_KEY_F21
KEY_F22 = cglfw3.GLFW_KEY_F22
KEY_F23 = cglfw3.GLFW_KEY_F23
KEY_F24 = cglfw3.GLFW_KEY_F24
KEY_F25 = cglfw3.GLFW_KEY_F25
KEY_KP_0 = cglfw3.GLFW_KEY_KP_0
KEY_KP_1 = cglfw3.GLFW_KEY_KP_1
KEY_KP_2 = cglfw3.GLFW_KEY_KP_2
KEY_KP_3 = cglfw3.GLFW_KEY_KP_3
KEY_KP_4 = cglfw3.GLFW_KEY_KP_4
KEY_KP_5 = cglfw3.GLFW_KEY_KP_5
KEY_KP_6 = cglfw3.GLFW_KEY_KP_6
KEY_KP_7 = cglfw3.GLFW_KEY_KP_7
KEY_KP_8 = cglfw3.GLFW_KEY_KP_8
KEY_KP_9 = cglfw3.GLFW_KEY_KP_9
KEY_KP_DECIMAL = cglfw3.GLFW_KEY_KP_DECIMAL
KEY_KP_DIVIDE = cglfw3.GLFW_KEY_KP_DIVIDE
KEY_KP_MULTIPLY = cglfw3.GLFW_KEY_KP_MULTIPLY
KEY_KP_SUBTRACT = cglfw3.GLFW_KEY_KP_SUBTRACT
KEY_KP_ADD = cglfw3.GLFW_KEY_KP_ADD
KEY_KP_ENTER = cglfw3.GLFW_KEY_KP_ENTER
KEY_KP_EQUAL = cglfw3.GLFW_KEY_KP_EQUAL
KEY_LEFT_SHIFT = cglfw3.GLFW_KEY_LEFT_SHIFT
KEY_LEFT_CONTROL = cglfw3.GLFW_KEY_LEFT_CONTROL
KEY_LEFT_ALT = cglfw3.GLFW_KEY_LEFT_ALT
KEY_LEFT_SUPER = cglfw3.GLFW_KEY_LEFT_SUPER
KEY_RIGHT_SHIFT = cglfw3.GLFW_KEY_RIGHT_SHIFT
KEY_RIGHT_CONTROL = cglfw3.GLFW_KEY_RIGHT_CONTROL
KEY_RIGHT_ALT = cglfw3.GLFW_KEY_RIGHT_ALT
KEY_RIGHT_SUPER = cglfw3.GLFW_KEY_RIGHT_SUPER
KEY_MENU = cglfw3.GLFW_KEY_MENU
KEY_LAST = cglfw3.GLFW_KEY_LAST
MOD_SHIFT = cglfw3.GLFW_MOD_SHIFT
MOD_CONTROL = cglfw3.GLFW_MOD_CONTROL
MOD_ALT = cglfw3.GLFW_MOD_ALT
MOD_SUPER = cglfw3.GLFW_MOD_SUPER
MOUSE_BUTTON_1 = cglfw3.GLFW_MOUSE_BUTTON_1
MOUSE_BUTTON_2 = cglfw3.GLFW_MOUSE_BUTTON_2
MOUSE_BUTTON_3 = cglfw3.GLFW_MOUSE_BUTTON_3
MOUSE_BUTTON_4 = cglfw3.GLFW_MOUSE_BUTTON_4
MOUSE_BUTTON_5 = cglfw3.GLFW_MOUSE_BUTTON_5
MOUSE_BUTTON_6 = cglfw3.GLFW_MOUSE_BUTTON_6
MOUSE_BUTTON_7 = cglfw3.GLFW_MOUSE_BUTTON_7
MOUSE_BUTTON_8 = cglfw3.GLFW_MOUSE_BUTTON_8
MOUSE_BUTTON_LAST = cglfw3.GLFW_MOUSE_BUTTON_LAST
MOUSE_BUTTON_LEFT = cglfw3.GLFW_MOUSE_BUTTON_LEFT
MOUSE_BUTTON_RIGHT = cglfw3.GLFW_MOUSE_BUTTON_RIGHT
MOUSE_BUTTON_MIDDLE = cglfw3.GLFW_MOUSE_BUTTON_MIDDLE
JOYSTICK_1 = cglfw3.GLFW_JOYSTICK_1
JOYSTICK_2 = cglfw3.GLFW_JOYSTICK_2
JOYSTICK_3 = cglfw3.GLFW_JOYSTICK_3
JOYSTICK_4 = cglfw3.GLFW_JOYSTICK_4
JOYSTICK_5 = cglfw3.GLFW_JOYSTICK_5
JOYSTICK_6 = cglfw3.GLFW_JOYSTICK_6
JOYSTICK_7 = cglfw3.GLFW_JOYSTICK_7
JOYSTICK_8 = cglfw3.GLFW_JOYSTICK_8
JOYSTICK_9 = cglfw3.GLFW_JOYSTICK_9
JOYSTICK_10 = cglfw3.GLFW_JOYSTICK_10
JOYSTICK_11 = cglfw3.GLFW_JOYSTICK_11
JOYSTICK_12 = cglfw3.GLFW_JOYSTICK_12
JOYSTICK_13 = cglfw3.GLFW_JOYSTICK_13
JOYSTICK_14 = cglfw3.GLFW_JOYSTICK_14
JOYSTICK_15 = cglfw3.GLFW_JOYSTICK_15
JOYSTICK_16 = cglfw3.GLFW_JOYSTICK_16
JOYSTICK_LAST = cglfw3.GLFW_JOYSTICK_LAST
NOT_INITIALIZED = cglfw3.GLFW_NOT_INITIALIZED
NO_CURRENT_CONTEXT = cglfw3.GLFW_NO_CURRENT_CONTEXT
INVALID_ENUM = cglfw3.GLFW_INVALID_ENUM
INVALID_VALUE = cglfw3.GLFW_INVALID_VALUE
OUT_OF_MEMORY = cglfw3.GLFW_OUT_OF_MEMORY
API_UNAVAILABLE = cglfw3.GLFW_API_UNAVAILABLE
VERSION_UNAVAILABLE = cglfw3.GLFW_VERSION_UNAVAILABLE
PLATFORM_ERROR = cglfw3.GLFW_PLATFORM_ERROR
FORMAT_UNAVAILABLE = cglfw3.GLFW_FORMAT_UNAVAILABLE
FOCUSED = cglfw3.GLFW_FOCUSED
ICONIFIED = cglfw3.GLFW_ICONIFIED
RESIZABLE = cglfw3.GLFW_RESIZABLE
VISIBLE = cglfw3.GLFW_VISIBLE
DECORATED = cglfw3.GLFW_DECORATED
RED_BITS = cglfw3.GLFW_RED_BITS
GREEN_BITS = cglfw3.GLFW_GREEN_BITS
BLUE_BITS = cglfw3.GLFW_BLUE_BITS
ALPHA_BITS = cglfw3.GLFW_ALPHA_BITS
DEPTH_BITS = cglfw3.GLFW_DEPTH_BITS
STENCIL_BITS = cglfw3.GLFW_STENCIL_BITS
ACCUM_RED_BITS = cglfw3.GLFW_ACCUM_RED_BITS
ACCUM_GREEN_BITS = cglfw3.GLFW_ACCUM_GREEN_BITS
ACCUM_BLUE_BITS = cglfw3.GLFW_ACCUM_BLUE_BITS
ACCUM_ALPHA_BITS = cglfw3.GLFW_ACCUM_ALPHA_BITS
AUX_BUFFERS = cglfw3.GLFW_AUX_BUFFERS
STEREO = cglfw3.GLFW_STEREO
SAMPLES = cglfw3.GLFW_SAMPLES
SRGB_CAPABLE = cglfw3.GLFW_SRGB_CAPABLE
REFRESH_RATE = cglfw3.GLFW_REFRESH_RATE
CLIENT_API = cglfw3.GLFW_CLIENT_API
CONTEXT_VERSION_MAJOR = cglfw3.GLFW_CONTEXT_VERSION_MAJOR
CONTEXT_VERSION_MINOR = cglfw3.GLFW_CONTEXT_VERSION_MINOR
CONTEXT_REVISION = cglfw3.GLFW_CONTEXT_REVISION
CONTEXT_ROBUSTNESS = cglfw3.GLFW_CONTEXT_ROBUSTNESS
OPENGL_FORWARD_COMPAT = cglfw3.GLFW_OPENGL_FORWARD_COMPAT
OPENGL_DEBUG_CONTEXT = cglfw3.GLFW_OPENGL_DEBUG_CONTEXT
OPENGL_PROFILE = cglfw3.GLFW_OPENGL_PROFILE
OPENGL_API = cglfw3.GLFW_OPENGL_API
OPENGL_ES_API = cglfw3.GLFW_OPENGL_ES_API
NO_ROBUSTNESS = cglfw3.GLFW_NO_ROBUSTNESS
NO_RESET_NOTIFICATION = cglfw3.GLFW_NO_RESET_NOTIFICATION
LOSE_CONTEXT_ON_RESET = cglfw3.GLFW_LOSE_CONTEXT_ON_RESET
OPENGL_ANY_PROFILE = cglfw3.GLFW_OPENGL_ANY_PROFILE
OPENGL_CORE_PROFILE = cglfw3.GLFW_OPENGL_CORE_PROFILE
OPENGL_COMPAT_PROFILE = cglfw3.GLFW_OPENGL_COMPAT_PROFILE
CURSOR = cglfw3.GLFW_CURSOR
STICKY_KEYS = cglfw3.GLFW_STICKY_KEYS
STICKY_MOUSE_BUTTONS = cglfw3.GLFW_STICKY_MOUSE_BUTTONS
CURSOR_NORMAL = cglfw3.GLFW_CURSOR_NORMAL
CURSOR_HIDDEN = cglfw3.GLFW_CURSOR_HIDDEN
CURSOR_DISABLED = cglfw3.GLFW_CURSOR_DISABLED
CONNECTED = cglfw3.GLFW_CONNECTED
DISCONNECTED = cglfw3.GLFW_DISCONNECTED
    

#
# Supplemental
#

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

cdef object _monitorfun
cdef void monitorfun_cb(cglfw3.GLFWmonitor* a,int b):
    global _monitorfun
    monitor = Monitor()
    monitor._this_ptr = a
    _monitorfun(monitor, b)


#
# Classes
#

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

def SetWindowSize(Window window, int width, int height):
    cglfw3.glfwSetWindowSize(<cglfw3.GLFWwindow*>window._this_ptr, width, height)

def GetFramebufferSize(Window window):
    cdef int width, height
    cglfw3.glfwGetFramebufferSize(<cglfw3.GLFWwindow*>window._this_ptr, &width, &height)
    return width, height

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

def GetInputMode(Window window, int mode):
    return cglfw3.glfwGetInputMode(<cglfw3.GLFWwindow*>window._this_ptr, mode)

def SetInputMode(Window window, int mode, int value):
    cglfw3.glfwSetInputMode(<cglfw3.GLFWwindow*>window._this_ptr, mode, value)

def GetKey(Window window, int key):
    return cglfw3.glfwGetKey(<cglfw3.GLFWwindow*>window._this_ptr, key)

def GetMouseButon(Window window, int button):
    return cglfw3.glfwGetMouseButton(<cglfw3.GLFWwindow*>window._this_ptr, button)

def GetCursorPos(Window window):
    cdef double x, y
    cglfw3.glfwGetCursorPos(<cglfw3.GLFWwindow*>window._this_ptr, &x, &y)
    return x, y

def SetCursorPos(Window window, double xpos, double ypos):
    cglfw3.glfwSetCursorPos(<cglfw3.GLFWwindow*>window._this_ptr, xpos, ypos)

def SetKeyCallback(Window window, cbfun):
    global _keyfuns
    _keyfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetKeyCallback(<cglfw3.GLFWwindow*>window._this_ptr, keyfun_cb)

def SetCharCallback(Window window, cbfun):
    global _charfuns
    _charfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetCharCallback(<cglfw3.GLFWwindow*>window._this_ptr, charfun_cb)

def SetMouseButtonCallback(Window window, cbfun):
    global _mousebuttonfuns
    _mousebuttonfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetMouseButtonCallback(<cglfw3.GLFWwindow*>window._this_ptr, mousebuttonfun_cb)

def SetCursorEnterCallback(Window window, cbfun):
    global _cursorenterfuns
    _cursorenterfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetCursorEnterCallback(<cglfw3.GLFWwindow*>window._this_ptr, cursorenterfun_cb)

def SetScrollCallback(Window window, cbfun):
    global _scrollfuns
    _scrollfuns[<size_t>window._this_ptr] = cbfun
    cglfw3.glfwSetScrollCallback(<cglfw3.GLFWwindow*>window._this_ptr, scrollfun_cb)

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

