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


# Not going to track how long key was pressed down since require spawning a timer thread for every key press
# May do it when create this project using a different library that implements key press listeners instead
# of needing to check state of the key.
# For now since this is personnel use, which just require starting a new line and specifying if want key held down.
# May provide option to specify time or just have it only release key when specify to on another line
# This isn't an exact typing recorder since need to specify actions want done for keys.
def record_key_presses(file_writing_to,exit_key = "esc", down_key_indicator = "DOWN:", up_key_indicator = "UP:", record_down_key_event = True, record_up_key_event = True):

    #note to self, reminder don't need ti invoke other functions here, only need to invoke them when reading file.

    key_tracker = {}
    example_file = file_writing_to

    no_exit_key = True

    while no_exit_key:
        for i in VK_CODE.keys():
            #https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getasynckeystate?redirectedfrom=MSDN
            #temp = win32api.GetAsyncKeyState(VK_CODE[i])
            #https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeystate
            temp = win32api.GetKeyState(VK_CODE[i])# since don't care about if key was pressed sincce last called
            # method, since documentation says shouldn't rely on it since other programs may call it also.

            if temp < 0:#Key is pressed down.
                if i in key_tracker.keys():
                    if key_tracker.get(i) == 0:#Last key check showed key was up, so we update its status.
                        key_tracker[i] = 1
                        if record_down_key_event:
                            example_file.write(f"{down_key_indicator}{i} ")
                        if i == exit_key:
                            no_exit_key = False
                            break
                        #print(i)
                        #print(f"{temp} \n")
                else:#This is a new key press during recording session.
                    key_tracker[i] = 1

            else:#Key is in up position.
                if i in key_tracker.keys():
                    if key_tracker.get(i) > 0:  # Last key check showed key was down, so we update its status.
                        key_tracker[i] = 0
                        if record_up_key_event:
                            example_file.write(f"{up_key_indicator}{i} ")
                        if i == exit_key:
                            no_exit_key = False
                            break
                        #print(f"updated to up: {i}")
                        #print(f"updated to up: {temp} \n")
                else:  # This is a new key press during recording session.
                    key_tracker[i] = 0

        #sleep(0.05)

    example_file.close()



# todo setup a function to read a file and call appropriate methods to press keys
"""
ts
pk
pkh
pkhr
rk
"""