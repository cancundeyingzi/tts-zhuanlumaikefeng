def 置顶窗口函数():
    hwnd_active = win32gui.GetForegroundWindow()
    global id
    id = hwnd_active
    win32gui.SetWindowPos(id, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOOWNERZORDER | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE);
    print('\033[31m置顶成功\033[0m')


def 取消置顶函数():
    hwnd_active = win32gui.GetForegroundWindow()
    global id
    id = hwnd_active
    win32gui.SetWindowPos(id, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOOWNERZORDER | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE);
    print('\033[31m取消置顶\033[0m')
