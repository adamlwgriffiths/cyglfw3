from __future__ import absolute_import, division, print_function, unicode_literals
import unittest
import cyglfw3 as glfw


class WindowTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        glfw.Init()
        # we need to avoid creating many window
        # because GLFW / NSApp begins to freak out and will segfault
        # good times, good times
        cls.window = glfw.CreateWindow(640, 480, 'Primary')

    @classmethod
    def tearDownClass(cls):
        glfw.DestroyWindow(cls.window)
        glfw.Terminate()

    def test_create_window(self):
        window = glfw.CreateWindow(640, 480, 'Create')
        glfw.DestroyWindow(window)

    @unittest.skip('not implemented')
    def test_window_size(self):
        pass

    def test_should_close(self):
        window = glfw.CreateWindow(640, 480, 'Should close')
        glfw.SetWindowShouldClose(window, True)
        self.assertTrue(glfw.WindowShouldClose(window))
        glfw.DestroyWindow(window)

    def test_info_strings(self):
        self.assertIsInstance(glfw.GetVersion(), tuple)
        self.assertIsInstance(glfw.GetVersionString(), str)

    @unittest.skip('not implemented')
    def test_primary_monitor(self):
        # test getting and using primary monitor
        pass

    def test_get_monitors_test_fullscreen(self):
        monitors = glfw.GetMonitors()
        for monitor in monitors:
            self.assertIsInstance(glfw.GetMonitorName(monitor),str)
            x,y = glfw.GetMonitorPos(monitor)
            width, height = glfw.GetMonitorPhysicalSize(monitor)
            window = glfw.CreateWindow(width, height, 'Monitors', monitor)
            glfw.DestroyWindow(window)

    def test_window_share(self):
        # test the window parameter of the createWindow function
        window = glfw.CreateWindow(640, 480, 'Share2', window=self.window)
        glfw.DestroyWindow(window)

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

        glfw.SetWindowSizeCallback(self.window, w_callback)
        glfw.SetFramebufferSizeCallback(self.window, f_callback)
        glfw.SetWindowSize(self.window, 800, 600)
        glfw.PollEvents()
        glfw.SetWindowSizeCallback(self.window, None)
        glfw.SetFramebufferSizeCallback(self.window, None)
        self.assertTrue(w_called[0])
        self.assertTrue(f_called[0])

    def test_window_pos_callback(self):
        called = [False]
        def callback(window, width, height):
            called[0] = True

        glfw.SetWindowPosCallback(self.window, callback)
        glfw.SetWindowPos(self.window, 10, 50)
        glfw.PollEvents()
        glfw.SetWindowPosCallback(self.window, None)
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

        glfw.SetWindowIconifyCallback(self.window, callback)
        glfw.IconifyWindow(self.window)
        glfw.PollEvents()
        glfw.RestoreWindow(self.window)
        glfw.SetWindowIconifyCallback(self.window, None)
        self.assertTrue(called[0])
        self.assertTrue(called[1])

    def test_show_hide(self):
        self.assertTrue(glfw.GetWindowAttrib(self.window, glfw.VISIBLE))
        glfw.HideWindow(self.window)
        self.assertFalse(glfw.GetWindowAttrib(self.window, glfw.VISIBLE))
        glfw.ShowWindow(self.window)
        self.assertTrue(glfw.GetWindowAttrib(self.window, glfw.VISIBLE))

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

    def test_mouse_buttons(self):
        glfw.GetMouseButton(self.window, 0)

    @unittest.skip('No test')
    def test_joystick(self):
        # names, pos, buttons
        pass

if __name__ == '__main__':
    unittest.main()
