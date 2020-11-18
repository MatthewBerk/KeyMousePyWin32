import win32con

from keymouse import mouseclicker, inputkeys
from time import sleep
import win32api

if __name__ == '__main__':

    """
    x, y = win32api.GetCursorPos()
    print(x)
    print(y)
    """

    inputkeys.record_key_presses()

    sleep(5)

    x, y = win32api.GetCursorPos()
    print(x)
    print(y)



    #sleep(3)
    #x2, y2 = win32api.GetCursorPos()

    # win32api.SetCursorPos((x, y))
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    # sleep(0.01)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    #
    # win32api.SetCursorPos((x2, y2))
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x2, y2, 0, 0)
    # sleep(0.01)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x2, y2, 0, 0)

    #mouseclicker.click_at_current_pos()

    #mouseclicker.click_at_current_pos(delay=10, times= 2)

    s = "."
    print(s.islower())
    print(s.isupper())

    #inputkeys.press_keys_and_hold(["a"])


    #mouseclicker.click_at(262,815)
    #sleep(0.05)
    #mouseclicker.click_at(662, 817)


    #mouseclicker.click_at_current_pos(times=1000)
