from time import sleep
import win32api
import win32con


# todo implement feature where can record mouse positions and whether you click or not
#  so that you can make a proper tester setup instead of manually tracking and writing cords.
# Would be creating a macro

#todo make this a class so can specify SLEEP_TIME for certain objects, OR allow passing in value to determine time to wait between releasing mouse key
SLEEP_TIME = 0.05  # Helps reduce likelihood of keys being pressed out of order and making sure key is pressed.

def click_at(x, y, times=1, delay=0.05):
    # https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setcursorpos
    win32api.SetCursorPos((x, y))
    while (times > 0):
        times -= 1
        sleep(delay)
        # https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)  # Coordinates seem to only matter when doing
        # mouse move. So could pass 0 without affecting anything.
        sleep(SLEEP_TIME)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click_at_current_pos(times=1, delay=0.05):
    # https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getcursorpos
    x, y = win32api.GetCursorPos()
    while (times > 0):
        times -= 1
        sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        sleep(SLEEP_TIME)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


# For if want to drag an item/application to a new spot
def click_and_move(x1, y1, x2, y2, times=1, delayrepeat=0.05, delaydrag=0.5):
    while (times > 0):
        times -= 1
        sleep(delayrepeat)
        win32api.SetCursorPos((x1, y1))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1, 0, 0)
        sleep(delaydrag)
        win32api.SetCursorPos((x2, y2))
        sleep(SLEEP_TIME)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x2, y2, 0, 0)

