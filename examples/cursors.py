#!/usr/bin/env python
from __future__ import division

from OpenGL import GL
from cyglfw3.compatible import *

if not glfwInit():
    exit(1)

window = glfwCreateWindow(640, 480, "Simple Example")
if not window:
    glfwTerminate()
    exit(1)

w, h = 32, 32
pixels = [[(255*(x/w), 255*(y/h), 0) for x in range(w)] for y in range(h)]

cursor = glfwCreateCursor(glfwImage(pixels), w/2, h/2)
glfwSetCursor(window, cursor)

glfwMakeContextCurrent(window)
while not glfwWindowShouldClose(window):
    width = 680
    height = 480
    
    GL.glViewport(0, 0, width, height)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    glfwSwapBuffers(window)
    glfwPollEvents()

glfwDestroyCursor(cursor)
glfwDestroyWindow(window)
glfwTerminate()
exit()