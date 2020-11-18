import win32con
import win32api
from time import sleep
from keymouse.vkcodes import VK_CODE



# Not using win32api.VkKeyScan because I am dealing with all
# keys on the keyboard, not just characters.
# Would be useful for programs where just care about characters

# i = "w"
# win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)
# Works for some DirectX games like Euro Truck Simulator 2  and other applications like notepad.
# Works for games like 7 days to die and Stardew Valley.
#
#
# So going with
# win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)
# to be on the safe side since have not found a downside to sending both vk code and scan code.


def type_out_string(string: str, delay_between_presses=0.05, delay_between_releases=0.05):
    """
    Invokes key events to type out word as if were typing it out on a physical keyboard.
    Ex: type_out_string("shift") would have the word shift typed out, not press the shift key.
    :param string: Word or sentence want typed out.
    :param delay_between_presses: Time to wait before press a key when about to press a key.
    :param delay_between_releases: Time to wait before releasing a key when about to release it.
    """
    for character in string:
        vkcode, needshift = identify_correct_key(character)
        if needshift:
            sleep(delay_between_presses)
            # http://timgolden.me.uk/pywin32-docs/win32api__keybd_event_meth.html
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0), 0, 0)
        sleep(delay_between_presses)
        win32api.keybd_event(vkcode, win32api.MapVirtualKey(vkcode, 0), 0, 0)
        sleep(delay_between_releases)
        win32api.keybd_event(vkcode, win32api.MapVirtualKey(vkcode, 0), win32con.KEYEVENTF_KEYUP, 0)
        if needshift:
            sleep(delay_between_releases)
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0),
                                 win32con.KEYEVENTF_KEYUP, 0)


def press_keys(collection_of_keys, delay_between_presses=0.05, delay_between_releases=0.05):
    """
    Presses and then releases key for each key in collection.
    Ex: press_keys(["shift"]) will have shift key pressed, not type out shift.
    Ex: press_keys(["H","e","l","l","o")  to have Hello typed. Should use type_out_string if want to type out words.
    :param collection_of_keys: A collection of strings which are names of keyboard keys.
    :param delay_between_presses: Time to wait before press a key when about to press a key.
    :param delay_between_releases: Time to wait before releasing a key when about to release it.
    """
    for key in collection_of_keys:
        vkcode, needshift = identify_correct_key(key)
        if needshift:
            sleep(delay_between_presses)
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0), 0, 0)
        sleep(delay_between_presses)
        win32api.keybd_event(vkcode, win32api.MapVirtualKey(vkcode, 0), 0, 0)
        sleep(delay_between_releases)
        win32api.keybd_event(vkcode, win32api.MapVirtualKey(vkcode, 0), win32con.KEYEVENTF_KEYUP, 0)
        if needshift:
            sleep(delay_between_releases)
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0),
                                 win32con.KEYEVENTF_KEYUP, 0)


def press_keys_and_hold(collection_of_keys, delay_between_presses=0.05, delay_between_shift_release=0.05):
    """
    Presses and holds key down for all keys in collection.
    Keeping key pressed won't cause key to be invoked several times (i.e. won't get several a's by holding a key down.)
    Does press and release shift key, if the key specified requires shift state.
    :param collection_of_keys: A collection of strings which are names of keyboard keys.
    :param delay_between_presses: Time to wait before press a key when about to press a key.
    :param delay_between_shift_release: Time to wait before releasing the shift key when about to release it.
    """
    for key in collection_of_keys:
        vkcode, needshift = identify_correct_key(key)
        if needshift:
            sleep(delay_between_presses)
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0), 0, 0)
        sleep(delay_between_presses)
        win32api.keybd_event(vkcode, win32api.MapVirtualKey(vkcode, 0), 0, 0)
        if needshift:
            sleep(delay_between_shift_release)
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0),
                                 win32con.KEYEVENTF_KEYUP, 0)


def press_keys_hold_and_release(collection_of_keys, delay_between_presses=0.05, delay_between_releases=0.05):
    """
    Presses and holds key down and then releases them after all keys in collection are pressed down.
    Note can't do ctrl+alt+del since it is a special key sequence known as the secure attention sequence
    Currently not going to set things up so program can invoke that sequence.
    :param collection_of_keys: A collection of strings which are names of keyboard keys.
    :param delay_between_presses: Time to wait before press a key when about to press a key.
    :param delay_between_releases: Time to wait before releasing a key when about to release it.
    """
    press_keys_and_hold(collection_of_keys, delay_between_presses, delay_between_releases)
    release_keys(collection_of_keys, delay_between_releases)


def release_keys(collection_of_keys, delay_between_releases=0.05):
    """
    Stops key press for each key in collection.
    :param collection_of_keys: A collection of strings which are names of keyboard keys.
    :param delay_between_releases: Time to wait before releasing a key when about to release it.
    """
    for key in collection_of_keys:
        vkcode, needshift = identify_correct_key(key)
        sleep(delay_between_releases)
        win32api.keybd_event(vkcode, win32api.MapVirtualKey(vkcode, 0), win32con.KEYEVENTF_KEYUP, 0)


def identify_correct_key(key: str):
    """
    Identifies the VK code of key passed in and if need to press shift key to access it
    Ex: $ requires VK code of 4 key and need to have shift button pressed.

    Can pass both name of character keys and non character keys like F1.

    :param key: name of key want to know proper VK code of
    :return: tuple
        - int: VKcode of key
        - boolean: if need shift key pressed
    """
    if key == ' ':
        return VK_CODE['spacebar'], False

    if len(key) == 1 and key.islower():  # is a lower case letter
        return VK_CODE[key], False
    if len(key) == 1 and key.isupper():  # is a upper case letter
        return VK_CODE[key.lower()], True

    if len(key) == 1:  # '\\' will still be true
        if key == '~':
            return VK_CODE['`'], True
        elif key == '!':
            return VK_CODE['1'], True
        elif key == '@':
            return VK_CODE['2'], True
        elif key == '#':
            return VK_CODE['3'], True
        elif key == '$':
            return VK_CODE['4'], True
        elif key == '%':
            return VK_CODE['5'], True
        elif key == '^':
            return VK_CODE['6'], True
        elif key == '&':
            return VK_CODE['7'], True
        elif key == '*':
            return VK_CODE['8'], True
        elif key == '(':
            return VK_CODE['9'], True
        elif key == ')':
            return VK_CODE['0'], True
        elif key == '_':
            return VK_CODE['-'], True
        elif key == '+':  # There is a vk code for + but not = but need to hold shift to get +.
            return VK_CODE['+'], True
        elif key == '=':
            return VK_CODE['+'], False
        elif key == '{':
            return VK_CODE['['], True
        elif key == '}':
            return VK_CODE[']'], True
        elif key == '|':
            return VK_CODE['\\'], True
        elif key == ':':
            return VK_CODE[';'], True
        elif key == '"':
            return VK_CODE['\''], True
        elif key == '<':
            return VK_CODE[','], True
        elif key == '>':
            return VK_CODE['.'], True
        elif key == '?':
            return VK_CODE['/'], True
        else:
            return VK_CODE[key], False

    else:  # is a non character key
        return VK_CODE[key], False



# So I found possibly a better way to record keys, using  a library called keyboard. Though it using ctypes
# so may use it when creating this project again but using ctypes instead of win32api.
# Current issue with this is due to speed at which checks, sometimes it print key twice when only press it oncce
# and when hit left shift, shift then left_shift gets printed.
# Try a few experiments and see if GetKeyState would be better for what you want.
#  otherwise may just have to stick with slow input where take input from user and they specify if they are going
#  to press a non character key (excluding when hold shift to get certain characters)
# Also look into GetKeyboardState
def record_key_presses(exit_key = "esc"):
    while True:
        for i in VK_CODE.keys():
            #https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getasynckeystate?redirectedfrom=MSDN
            if win32api.GetAsyncKeyState(VK_CODE[i]):
                print(i)
        sleep(0.1)

# todo setup a function to read a file and call apropiate methods to press keys
"""
ts
pk
pkh
pkhr
rk
"""