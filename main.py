import win32con

from keymouse import mouseclicker, inputkeys
from time import sleep
import win32api

#Decided I wanted to have the ability to record keyboard and mouse events to same file
def start_recording_session(filepath):
    example_file = open(filepath, "w")
    keep_recording = True
    while keep_recording:
        val = input("Type k for recording keyboard. Type m for recording mouse. Type d if done: ")
        if val == "k":
            print("KEY \n",
                  "ts: Just typing out a word or sentence, not pressing non-character keys excluding shift.\n",
                  "pk: Pressing any key on keyboard.\n",
                  "pkh: Want key you entered to be held down until release.\n",
                  "rk: Release key you entered.\n")

            decision = input("Type action your going to perform so can properly record key presses: ")
            #todo will just write to file indicating type of action (so when create function to read file, know what methouds to call).
            # todo ALSO write if its keyboard or mouse!!!!
            if decision == "ts":
                print()
            elif decision == "pk":#todo make edit to allow for specifying time, if don't specify then will only release key when rk for key is invoked
                print()
            elif decision == "pkh":
                print()
            elif decision == "rk":
                print()
            else:
                print(f"{decision} is not a valid input!")
        elif val == "m":
            print()
        elif val == "d":
            keep_recording = False
        else:
            print(f"{val} is not a valid input!")

#todo setup function to read file.


if __name__ == '__main__':

    """
    x, y = win32api.GetCursorPos()
    print(x)
    print(y)
    """


    sleep(5)
    print("Ready to test")

    inputkeys.record_key_presses()

    #sleep(5)

    # x, y = win32api.GetCursorPos()
    # print(x)
    # print(y)



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

    # s = "."
    # print(s.islower())
    # print(s.isupper())

    #inputkeys.press_keys_and_hold(["a"])


    #mouseclicker.click_at(262,815)
    #sleep(0.05)
    #mouseclicker.click_at(662, 817)


    #mouseclicker.click_at_current_pos(times=1000)
