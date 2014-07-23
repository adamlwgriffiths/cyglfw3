from OpenGL import GL
import cyglfw3 as glfw

if not glfw.Init():
    exit()

version = 4,1

glfw.WindowHint(glfw.CONTEXT_VERSION_MAJOR, version[0])
glfw.WindowHint(glfw.CONTEXT_VERSION_MINOR, version[1])
glfw.WindowHint(glfw.OPENGL_FORWARD_COMPAT, 1)
glfw.WindowHint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

window = glfw.CreateWindow(640, 480, 'Hello World')
if not window:
    glfw.Terminate()
    print 'Failed to create window'
    exit()

glfw.MakeContextCurrent(window)
print GL.glGetString(GL.GL_VERSION)

glfw.DestroyWindow(window)
glfw.Terminate()
