from __future__ import print_function
from OpenGL import GL
import cyglfw3 as glfw

if not glfw.Init():
    exit()

version = 3,2

glfw.WindowHint(glfw.CONTEXT_VERSION_MAJOR, version[0])
glfw.WindowHint(glfw.CONTEXT_VERSION_MINOR, version[1])
glfw.WindowHint(glfw.OPENGL_FORWARD_COMPAT, 1)
glfw.WindowHint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

windows = [
    glfw.CreateWindow(640, 480, 'Hello World {}'.format(count))
    for count in range(2)
]

if not windows:
    glfw.Terminate()
    print('Failed to create window')
    exit()

glfw.SetWindowPos(windows[0], 0, 0)
w, h = glfw.GetWindowSize(windows[0])
glfw.SetWindowPos(windows[1], w, 0)

def update_windows():
    for window in windows:
        if glfw.WindowShouldClose(window):
            return
        glfw.MakeContextCurrent(window)
        GL.glClearColor(0.2, 0.2, 0.2, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        glfw.SwapBuffers(window)

glfw.MakeContextCurrent(windows[0])
print('GL:',GL.glGetString(GL.GL_VERSION))
print('GLFW3:',glfw.GetVersionString())
for iteration in range(100):
    update_windows()
    glfw.PollEvents()

for window in windows:
    glfw.DestroyWindow(window)

glfw.Terminate()
