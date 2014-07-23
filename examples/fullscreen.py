from __future__ import print_function
from OpenGL import GL
import cyglfw3 as glfw

if not glfw.Init():
    exit()

version = 2,1

glfw.WindowHint(glfw.CONTEXT_VERSION_MAJOR, version[0])
glfw.WindowHint(glfw.CONTEXT_VERSION_MINOR, version[1])

monitor = glfw.GetPrimaryMonitor()
window = glfw.CreateWindow(640, 480, 'Hello World', monitor)
if not window:
    glfw.Terminate()
    print('Failed to create window')
    exit()

glfw.MakeContextCurrent(window)
print('GL:',GL.glGetString(GL.GL_VERSION))
print('GLFW3:',glfw.GetVersionString())
for iteration in range(100):
    if glfw.WindowShouldClose(window):
        break
    GL.glClearColor(0.2, 0.2, 0.2, 1.0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    glfw.SwapBuffers(window)
    glfw.PollEvents()

glfw.DestroyWindow(window)
glfw.Terminate()
