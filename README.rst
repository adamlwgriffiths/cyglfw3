=======
CyGLFW3
=======

Python bindings for `GLFW 3+ <http://www.glfw.org>`_ using Cython.

Provides an API which matches the C API.

Differences
===========

* Enumerations have dropped their "GLFW\_" prefix.
* Functions have dropped their "glfw" prefix.
* {Get|Set}UserPointer is not accessible as it doesn't make sense for Python.
* The {Get|Set}Time functions are available but Python's time module should be used in preference.


C Code
======

::

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

        glfwMakeContextCurrent(window);
        while (!glfwWindowShowClose(window))
        {
            /* Render here */

            /* Display the render buffer */
            glfwSwapBuffers(window);

            /* Pump the message queue */
            glfwPollEvents();
        }

        /* Shutdown */
        glfwTerminate();
        return 0;
    }


Python Code
===========

::

    # needed if you're running the OS-X system python
    try:
        from AppKit import NSApp, NSApplication
    except:
        pass

    import cyglfw3 as glfw
    if not glfw.Init():
        exit()

    window = glfw.CreateWindow(640, 480, 'Hello World')
    if not window:
        glfw.Terminate()
        exit()

    glfw.MakeContextCurrent(window)
    while not glfw.WindowShouldClose(window):
        # Render here

        # Swap front and back buffers
        glfw.SwapBuffers(window)

        # Poll for and process events
        glfw.PollEvents()

    glfw.Terminate()


Prefix Compatible Code
======================

A compatibility layer is provided to be 1:1 compatible with other GLFW3 wrappers.
Commonly, these don't drop the `GLFW_` prefix from constants, nor the `glfw` prefix
from functions.

To use the compatibility module, use `import cyglfw3.compatible as glfw`::

    # needed if you're running the OS-X system python
    try:
        from AppKit import NSApp, NSApplication
    except:
        pass

    import cyglfw3.compatible as glfw
    if not glfw.glfwInit():
        exit()

    window = glfw.glfwCreateWindow(640, 480, 'Hello World')
    if not window:
        glfw.glfwTerminate()
        exit()

    glfw.glfwMakeContextCurrent(window)
    while not glfw.glfwWindowShouldClose(window):
        # Render here

        # Swap front and back buffers
        glfw.glfwSwapBuffers(window)

        # Poll for and process events
        glfw.glfwPollEvents()

    glfw.glfwTerminate()


Installation
============

::

    pip install cyglfw3


Manual Building
===============

If you have trouble building CyGLFW3, please raise an issue on Github.

When specifying the include path, ensure that the GLFW directory is a sub-directory
of that path.
For example: the path /usr/local/include/GLFW would use include /usr/local/include

The lib path should contain the glfw library file.


OS-X / Linux
------------

CyGLFW3 provides support for OS-X `Homebrew <http://brew.sh/>`_ and `MacPorts <https://www.macports.org/>`_.

Linux builds should work with any package manager.

::

    python setup.py build_ext -i


Specifying an alternate GLFW installation path:

::

    env CPATH=<include path> LIBRARY_PATH=<lib path> python setup.py build_ext -i


Windows
-------

The following commands are untested, please report their success or failure.

::

    set GLFW_ROOT=<path to include/GLFW/glfw3.h>
    python setup.py build_ext -i

If you get `ImportError: DLL load failed: The specified procedure could not be found.`
Please place the glfw3.dll from `lib-vc2012` in the installation path.


Common Problems
===============

- PyOpenGL reports the OpenGL version as None and my GL functions do nothing!

You _must_ set an active context or your OpenGL calls will go no where::

    glfw.MakeContextCurrent(window)


This is by design in GLFW3.


Dependencies
============

* Python 2.7 / 3.4
* Cython
* GLFW 3

