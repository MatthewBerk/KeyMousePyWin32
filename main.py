# Works for regular applications and games using DirectX
# Can't specify application, sends keys/mouse clicks to active application

from keymouse import mouseclicker, inputkeys
from time import sleep

if __name__ == '__main__':
    sleep(2)
    i = 'a'
    mouseclicker.click_at_current_pos()
    inputkeys.press_keys(i)

