#!/usr/bin/env python
from OpenGL import GL as gl
from cyglfw3.compatible import *

if not glfwInit():
    exit(1)

window = glfwCreateWindow(640, 480, "Simple Example")
if not window:
    glfwTerminate()
    exit(1)

def key_callback(window, key, scancode, action, mods):
    if (key == GLFW_KEY_ESCAPE and action == GLFW_PRESS):
        glfwSetWindowShouldClose(window, gl.GL_TRUE)

glfwSetKeyCallback(window, key_callback)

glfwMakeContextCurrent(window)
while not glfwWindowShouldClose(window):
    width = 680
    height = 480
    # frame_size = glfwGetFrameBufferSize(window, width, height)
    ratio = width / float(height)

    gl.glViewport(0, 0, width, height)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-ratio, ratio, -1.0, 1.0, 1.0, -1.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)

    gl.glLoadIdentity()
    gl.glRotatef(float(glfwGetTime() * 50), 0, 0, 1)

    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(1.0, 0.0, 0.0)
    gl.glVertex3f(-0.6, -0.4, 0.0)
    gl.glColor3f(0.0, 1.0, 0.0)
    gl.glVertex3f(0.6, -0.4, 0.0)
    gl.glColor3f(0.0, 0.0, 1.0)
    gl.glVertex3f(0.0, 0.6, 0.0)
    gl.glEnd()

    glfwSwapBuffers(window)
    glfwPollEvents()

glfwDestroyWindow(window)
glfwTerminate()
exit()
