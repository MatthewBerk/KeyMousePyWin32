from keymouse import mouseclicker, inputkeys
from time import sleep
import win32api

if __name__ == '__main__':

    """
    x, y = win32api.GetCursorPos()
    print(x)
    print(y)
    """

    sleep(8)

    x, y = win32api.GetCursorPos()
    print(x)
    print(y)

    mouseclicker.click_at_current_pos()

    s = "."
    print(s.islower())
    print(s.isupper())

    inputkeys.press_keys_and_hold(["a"])


    #mouseclicker.click_at(262,815)
    #sleep(0.05)
    #mouseclicker.click_at(662, 817)


    #mouseclicker.click_at_current_pos(times=1000)
