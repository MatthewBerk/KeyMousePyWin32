import win32con
import win32api
from time import sleep
from keymouse.vkcodes import VK_CODE

# Not using win32api.VkKeyScan because I am dealing with all
# keys on the keyboard, not just characters.
# Would be useful for programs where just care about characters

# i = "w"
# win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)#Works for some DirectX games like Euro Truck Simulator 2  and other applications like notepad.
# Works for games like 7 days to die and Stardew Valley.
#
#
# So going with
# win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)
# to be on the safe side since have not found a downside to sending both vk code and scan code.

#Todo maybe make this a class so can change SLEEP_TIME for objects, or also passing value for time to wait between keypresses and key releases
SLEEP_TIME = 0.05  # Helps reduce likelihood of keys being pressed out of order and making sure key is pressed.


def type_out_string(string: str):
    '''
    Invokes key events to type out word as if were typing it out on a physical keyboard.
    Ex: type_out_string("shift") would have the word shift typed out, not press the shift key.
    :param string: Word or sentence want typed out.
    '''
    for character in string:
        vkcode, needshift = identify_correct_key(character)
        sleep(SLEEP_TIME)
        if needshift:
            # http://timgolden.me.uk/pywin32-docs/win32api__keybd_event_meth.html
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0), 0, 0)
        sleep(SLEEP_TIME)
        win32api.keybd_event(vkcode, win32api.MapVirtualKey(vkcode, 0), 0, 0)
        sleep(SLEEP_TIME)
        win32api.keybd_event(vkcode, win32api.MapVirtualKey(vkcode, 0), win32con.KEYEVENTF_KEYUP, 0)
        if needshift:
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0),
                                 win32con.KEYEVENTF_KEYUP, 0)


def press_keys(collectionkeys):
    """
    Presses and then releases key for each key in collection.
    Ex: press_keys(["shift"]) will have shift key pressed, not type out shift.
    Ex: press_keys(["H","e","l","l","o")  to have Hello typed. Should use type_out_string if want to type out words.
    :param collectionkeys: A collection of strings which are names of keys
    """
    for key in collectionkeys:
        vkcode, needshift = identify_correct_key(key)
        sleep(SLEEP_TIME)
        if needshift:
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0), 0, 0)
        sleep(SLEEP_TIME)
        win32api.keybd_event(vkcode, win32api.MapVirtualKey(vkcode, 0), 0, 0)
        sleep(SLEEP_TIME)
        win32api.keybd_event(vkcode, win32api.MapVirtualKey(vkcode, 0), win32con.KEYEVENTF_KEYUP, 0)
        sleep(SLEEP_TIME)
        if needshift:
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0),
                                 win32con.KEYEVENTF_KEYUP, 0)


def press_keys_and_hold(collectionkeys):
    """
    Presses and holds key down for all keys in collection.
    Keeping key pressed won't cause key to be invoked several times (i.e. won't get several a's by holding a key down.)
    :param collectionkeys: A collection of strings which are names of keys.
    """
    for key in collectionkeys:
        vkcode, needshift = identify_correct_key(key)
        sleep(SLEEP_TIME)
        if needshift:
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0), 0, 0)
        sleep(SLEEP_TIME)
        win32api.keybd_event(vkcode, win32api.MapVirtualKey(vkcode, 0), 0, 0)
        sleep(SLEEP_TIME)
        if needshift:
            win32api.keybd_event(VK_CODE['left_shift'], win32api.MapVirtualKey(VK_CODE['left_shift'], 0),
                                 win32con.KEYEVENTF_KEYUP, 0)


def press_keys_hold_and_release(collectionkeys):
    """
    Presses and holds key down and then releases them after all keys in collection are pressed down.
    Note can't do ctrl+alt+del since it is a special key sequence known as the secure attention sequence
    Currently not going to set things up so program can invoke that sequence.
    :param collectionkeys: A collection of strings which are names of keys
    """
    press_keys_and_hold(collectionkeys)
    release(collectionkeys)


def release(collectionkeys):
    """
    Stops key press for each key in collection.
    :param collectionkeys: A collection of strings which are names of keys
    """
    for key in collectionkeys:
        sleep(SLEEP_TIME)
        vkcode, needshift = identify_correct_key(key)
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
