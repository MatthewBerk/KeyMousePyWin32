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

    s = "."
    print(s.islower())
    print(s.isupper())

    #inputkeys.press_keys_and_hold("a")

    print(inputkeys.identify_correct_key.__doc__)

    #inputkeys.type_out_string("shift")

    inputkeys.press_keys_and_hold(["ctrl","alt","del"])

    #inputkeys.identify_correct_key()

    #mouseclicker.click_at(262,815)
    #sleep(0.05)
    #mouseclicker.click_at(662, 817)


    #mouseclicker.click_at_current_pos(times=1000)


    #i = 'ab'
    #inputkeys.press_keys(i)

    #mouseclicker.click_and_move(2534,499,2355,498)

