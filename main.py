# Works for regular applications and games using DirectX
# Can't specify application, sends keys/mouse clicks to active application

from keymouse import mouseclicker, inputkeys
from time import sleep
import win32api

if __name__ == '__main__':

    """
    x, y = win32api.GetCursorPos()
    print(x)
    print(y)
    """



    sleep(2)



    #i = 'a'
    #mouseclicker.click_at_current_pos()
    #inputkeys.press_keys(i)

    mouseclicker.click_and_move(2534,499,2355,498)

