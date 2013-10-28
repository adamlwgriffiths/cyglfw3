CyGLFW3
=======

Python bindings for GLFW 3+ using Cython.

A trivial API which matches the C API.


C Code
------

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

Python Code
-----------

```
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

Dependencies
------------

   * Python 2.7
   * Cython
   * GLFW 3
