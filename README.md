#CyGLFW3

Python bindings for GLFW 3+ using Cython.

Provides an API which matches the C API.

##Differences
   * Enumerations have dropped their 'GLFW_' prefix.
   * Functions have dropped their 'glfw' prefix.
   * {Get|Set}UserPointer is not accessible as it doesn't make sense for Python.
   * The {Get|Set}Time functions are available but Python's time module should be
   used in preference.


##C Code

```
#include <GLFW/glfw3.h>
int main(void)
{
    GLFWwindow* window;

    /* Initialize the library */
    if (!glfwInit())
        return -1;

    /* Create a windowed mode window and its OpenGL context */
    window = glfwCreateWindow(640, 480, "Hello World", NULL, NULL);

    if (!window)
    {
        glfwTerminate();
        return -1;
    }

    glfwTerminate();
    return 0;
}
```

##Python Code

```
# needed if you're running the OS-X system python
try:
  from AppKit import NSApp, NSApplication
except:
  pass

import cyglfw3 as glfw
if not glfw.init():
    exit()

window = glfw.createWindow(640, 480, 'Hello World')
if not window:
    glfw.terminate()
    exit()

glfw.makeContextCurrent(window)
while not glfw.windowShouldClose(window):
    # Render here

    # Swap front and back buffers
    glfw.swapBuffers(window)

    # Poll for and process events
    glfw.pollEvents()

glfw.terminate()
```


##Building

CyGLFW has only been tested on OS-X.
Please provide any errors so more platforms can be supported.

When specifying the include path, ensure that the GLFW directory is a sub-directory
of that path.
For example: the path /usr/local/include/GLFW would use include /usr/local/include

The lib path should contain the glfw library file.


### OS-X / Linux

The setup.py script add's includes for homebrew's GLFW location (/usr/local/include and /usr/local/lib)

```
python setup.py build_ext -i
```

Specifying an alternate GLFW installation path:
```
env CPATH=<path to headers> LIBRARY_PATH=<path to lib> python setup.py build_ext -i
```

### Windows

The following commands are untested, please report their success or failure.
```
set INCLUDE=%INCLUDE%;<path to headers>
set LIB=%LIB%;<path to lib>
python setup.py build_ext -i
```


##Dependencies

   * Python 2.7
   * Cython
   * GLFW 3

