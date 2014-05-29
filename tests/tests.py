from __future__ import absolute_import, division, print_function, unicode_literals
import unittest
import time
import cyglfw3 as glfw


class WindowTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        glfw.init()
        # we need to avoid creating many window
        # because GLFW / NSApp begins to freak out and will segfault
        # good times, good times
        cls.window = glfw.createWindow(640, 480, 'Primary')

    @classmethod
    def tearDownClass(cls):
        glfw.destroyWindow(cls.window)
        glfw.terminate()

    def test_create_window(self):
        window = glfw.createWindow(640, 480, 'Create')
        time.sleep(0.5)
        glfw.destroyWindow(window)

    def test_should_close(self):
        window = glfw.createWindow(640, 480, 'Should close')
        glfw.setWindowShouldClose(window, True)
        self.assertTrue(glfw.windowShouldClose(window))
        time.sleep(0.5)
        glfw.destroyWindow(window)

    def test_info_strings(self):
        self.assertIsInstance(glfw.getVersion(), tuple)
        self.assertIsInstance(glfw.getVersionString(), str)

    def test_get_monitors_test_fullscreen(self):
        monitors = glfw.getMonitors()
        for monitor in monitors:
            self.assertIsInstance(glfw.getMonitorName(monitor),str)
            x,y = glfw.getMonitorPos(monitor)
            width, height = glfw.getMonitorPhysicalSize(monitor)
            window = glfw.createWindow(width, height, 'Monitors', monitor)
            time.sleep(0.5)
            glfw.destroyWindow(window)
            time.sleep(0.5)

    def test_window_share(self):
        # test the window parameter of the createWindow function
        window = glfw.createWindow(640, 480, 'Share2', window=self.window)
        time.sleep(0.5)
        glfw.destroyWindow(window)

    @unittest.skip('No test')
    def test_input_mode(self):
        pass

    def test_window_framebuffer_resize_callback(self):
        w_called = [False]
        def w_callback(window, width, height):
            w_called[0] = True
        f_called = [False]
        def f_callback(window, width, height):
            f_called[0] = True

        glfw.setWindowSizeCallback(self.window, w_callback)
        glfw.setFramebufferSizeCallback(self.window, f_callback)
        glfw.setWindowSize(self.window, 800, 600)
        glfw.pollEvents()
        glfw.setWindowSizeCallback(self.window, None)
        glfw.setFramebufferSizeCallback(self.window, None)
        self.assertTrue(w_called[0])
        self.assertTrue(f_called[0])

    def test_window_pos_callback(self):
        called = [False]
        def callback(window, width, height):
            called[0] = True

        glfw.setWindowPosCallback(self.window, callback)
        glfw.setWindowPos(self.window, 10, 50)
        glfw.pollEvents()
        glfw.setWindowPosCallback(self.window, None)
        self.assertTrue(called[0])

    @unittest.skip('No test')
    def test_window_close_callback(self):
        pass

    @unittest.skip('No test')
    def test_window_refresh_callback(self):
        pass

    @unittest.skip('No test')
    def test_window_focus_callback(self):
        pass

    def test_window_iconify_callback(self):
        called = [False, False]
        def callback(window, iconified):
            called[int(iconified)] = True

        glfw.setWindowIconifyCallback(self.window, callback)
        glfw.iconifyWindow(self.window)
        glfw.pollEvents()
        glfw.restoreWindow(self.window)
        glfw.setWindowIconifyCallback(self.window, None)
        self.assertTrue(called[0])
        self.assertTrue(called[1])

    @unittest.skip('Causing segfauls, possible glfw issue on osx?')
    def test_show_hide(self):
        self.assertTrue(glfw.getWindowAttrib(self.window, glfw.VISIBLE))
        glfw.hideWindow(window)
        self.assertFalse(glfw.getWindowAttrib(self.window, glfw.VISIBLE))
        glfw.showWindow(window)
        self.assertTrue(glfw.getWindowAttrib(self.window, glfw.VISIBLE))

    @unittest.skip('No test')
    def test_char_callback(self):
        pass

    @unittest.skip('No test')
    def test_key_callback(self):
        pass

    @unittest.skip('No test')
    def test_cursor_callback(self):
        # cursor enter, pos
        # get cursor pos
        pass

    @unittest.skip('No test')
    def test_mouse_callback(self):
        # mouse button, pos, scroll
        pass

    @unittest.skip('Causing segfauls, possible glfw issue on osx?')
    def test_mouse_buttons(self):
        glfw.getMouseButton(window, 0)

    @unittest.skip('No test')
    def test_joystick(self):
        # names, pos, buttons
        pass

if __name__ == '__main__':
    unittest.main()
