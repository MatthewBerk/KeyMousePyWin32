import win32con
import win32api
from time import sleep
from keymouse.vkcodes import VK_CODE
from ctypes import windll

# Not using win32api.VkKeyScan because I am dealing with all
# keys on keyboard, not just characters.
# Would be useful for programs where just care about characters

'''
# Was Euro Truck Simulator 2 that lead me to discovering one and two, since before was using simple games.
i = "a"
win32api.keybd_event(0, win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)# Works for some directX games like Euro Truck Simulator 2 but not other applications like notepad.
# Doesn't work for games like 7 days to die which is reported to use DirectX. Works for Euro Truck Simulator 2.
sleep(3.05)
win32api.keybd_event(0, win32api.MapVirtualKey(VK_CODE[i], 0), win32con.KEYEVENTF_KEYUP, 0)

i = "w"
win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)#Works for some directX games like Euro Truck Simulator 2  and other applications like notepad.
# Works for games like 7 days to die and Stardew Valley.
sleep(3.05)
win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), win32con.KEYEVENTF_KEYUP, 0)

i = "d"
win32api.keybd_event(VK_CODE[i], 0, 0,0) #Doesn't work for some directX games like Euro Truck Simulator 2  BUT works for other applications like notepad.
# Works for games like 7 days to die and Stardew Valley.
sleep(3.05)
win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)

So going with
win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)
to be on safe side since have not found a downside to sending both vk code and scan code.
'''

# Pass a string you want typed out on keyboard.
# Ex: "My shift" will have keys m y s h i f t  presss on keyboard.
def typeout_string(value: str):
    return 1

# Pass a collection of keys that you wanted pressed. Collection must contain strings.
# Ex: press_keys(["shift"]) will have shift key pressed, not type out shift on keyboard.
def press_keys(keys):
    for i in keys:
        # http://timgolden.me.uk/pywin32-docs/win32api__keybd_event_meth.html
        win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)
        sleep(0.05)
        win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), win32con.KEYEVENTF_KEYUP, 0)


#Note pressing and holding a won't cause several a's to be written out!
def press_keys_and_hold(*keys):
    for i in keys:
        win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)
        sleep(0.05)


def press_keys_hold_and_release(*keys):
    press_keys_and_hold(keys)
    release(keys)


def release(*keys):
    for i in keys:
        win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), win32con.KEYEVENTF_KEYUP, 0)
        sleep(0.05)

# todo Eventually this function will determine what vk and scan code to send base on the strings passed.
#  Since the virtual and scan code for $ or A are the same as 4 and a, need to determine if need shift key held
#   Down or not. That is what this function is for. Plan to use it in all functions which will then
#    send the value to win32api.keybd_event, and also invoke shift key if needed. Want to be able to
#     Have the funcctionality of holding keys down, and releasing them while also handling the special characters
#      That need shift state.
def identify_correct_key():

    i = "w"
    win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)#Works for some directX games like Euro Truck Simulator 2  and other applications like notepad.
    # Works for games like 7 days to die and Stardew Valley.
    sleep(3.05)
    win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), win32con.KEYEVENTF_KEYUP, 0)


    return 1


# Use when want to send uppercase letters or special characters like $
# todo plan to have this be replaced by identify_correct_key, that way can keep functionality of
#  holding key down while not having duplicate code
def shift_press_keys(*keys: str):
    for i in keys:
        if i == ' ':
            win32api.keybd_event(VK_CODE['spacebar'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['spacebar'], 0, win32con.KEYEVENTF_KEYUP, 0)
            continue
        if i.islower():  # Only true for lower case letters.
            win32api.keybd_event(VK_CODE[i], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)
            continue

        win32api.keybd_event(VK_CODE['left_shift'], 0, 0, 0)

        if i.isupper():  # Only true for upper case letters.
            i = i.lower()
            win32api.keybd_event(VK_CODE[i], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '~':
            win32api.keybd_event(VK_CODE['`'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['`'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '!':
            win32api.keybd_event(VK_CODE['1'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['1'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '@':
            win32api.keybd_event(VK_CODE['2'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['2'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '#':
            win32api.keybd_event(VK_CODE['3'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['3'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '$':
            win32api.keybd_event(VK_CODE['4'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['4'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '%':
            win32api.keybd_event(VK_CODE['5'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['5'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '^':
            win32api.keybd_event(VK_CODE['6'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['6'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '&':
            win32api.keybd_event(VK_CODE['7'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['7'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '*':
            win32api.keybd_event(VK_CODE['8'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['8'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '(':
            win32api.keybd_event(VK_CODE['9'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['9'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == ')':
            win32api.keybd_event(VK_CODE['0'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['0'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '_':
            win32api.keybd_event(VK_CODE['-'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['-'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '=':  # for some reason there is a vk code for + but not =.
            win32api.keybd_event(VK_CODE['+'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['+'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '{':
            win32api.keybd_event(VK_CODE['['], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['['], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '}':
            win32api.keybd_event(VK_CODE[']'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE[']'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '|':
            win32api.keybd_event(VK_CODE['\\'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['\\'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == ':':
            win32api.keybd_event(VK_CODE[';'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE[';'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '"':
            win32api.keybd_event(VK_CODE['\''], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['\''], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '<':
            win32api.keybd_event(VK_CODE[','], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE[','], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '>':
            win32api.keybd_event(VK_CODE['.'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['.'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '?':
            win32api.keybd_event(VK_CODE['/'], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE['/'], 0, win32con.KEYEVENTF_KEYUP, 0)
        else: #is a non character key such as enter
            win32api.keybd_event(VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)
            sleep(0.05)
            win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), win32con.KEYEVENTF_KEYUP, 0)

        win32api.keybd_event(VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
