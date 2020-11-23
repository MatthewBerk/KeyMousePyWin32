from time import sleep
import win32api
import win32con


# todo implement feature where can record mouse positions and whether you click or not
#  so that you can make a proper tester setup instead of manually tracking and writing cords.
# Would be creating a macro

def click_at(x, y, times=1, left_down_delay=0.05, left_up_delay=0.05):
    """
    :param x: Screen horizontal position want mouse cursor at
    :param y: Screen vertical position want mouse cursor at
    :param times: Number of Times want mouse clicked
    :param left_down_delay: Time to wait before press left mouse button when about to press it.
    :param left_up_delay: Time to wait before releasing left mouse button hen about to release it.
    """
    # https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setcursorpos
    win32api.SetCursorPos((x, y))
    while times > 0:
        times -= 1
        sleep(left_down_delay)
        # https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)  # Coordinates seem to only matter when doing
        # mouse move. So could pass 0 without affecting anything.
        sleep(left_up_delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click_at_current_pos(times=1, left_down_delay=0.05, left_up_delay=0.05):
    """
    :param times: Number of times want mouse clicked
    :param left_down_delay: Time to wait before press left mouse button when about to press it.
    :param left_up_delay: Time to wait before releasing left mouse button hen about to release it.
    """
    # https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getcursorpos
    x, y = win32api.GetCursorPos()
    while times > 0:
        times -= 1
        sleep(left_down_delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        sleep(left_up_delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click_and_move(x1, y1, x2, y2, times=1, left_down_delay=0.05, left_up_delay=0.05, drag_delay=0.5):
    """
    Use if want to drag mouse from one position to another, or drag an application.
    :param x1: Screen horizontal position want mouse cursor at initially
    :param y1: Screen vertical position want mouse cursor at initially
    :param x2: Screen horizontal position want mouse cursor at while holding left mouse button down.
    :param y2: Screen vertical position want mouse cursor at while holding left mouse button down.
    :param times: Number of times want to repeat this action
    :param left_down_delay: Time to wait before press left mouse button when about to press it.
    :param left_up_delay: Time to wait before releasing left mouse button hen about to release it.
    :param drag_delay: Time to wait before moving mouse cursor to second position specified.
    """
    while times > 0:
        times -= 1
        sleep(left_down_delay)
        win32api.SetCursorPos((x1, y1))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1, 0, 0)
        sleep(drag_delay)
        win32api.SetCursorPos((x2, y2))
        sleep(left_up_delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x2, y2, 0, 0)


def click_and_hold(x, y, left_down_delay=0.05):
    """
    :param x: Screen horizontal position want mouse cursor at
    :param y: Screen vertical position want mouse cursor at
    :param left_down_delay: Time to wait before press left mouse button when about to press it.
    """
    win32api.SetCursorPos((x, y))
    sleep(left_down_delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)


def click_and_hold_at_current_pos(left_down_delay=0.05):
    """
    :param left_down_delay: Time to wait before press left mouse button when about to press it.
    """
    x, y = win32api.GetCursorPos()
    sleep(left_down_delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)


# thinking will require using to hit a button to record mouse movements
# since otherwise could end up with a lot of mouse recordings unless do
#  time limit then I may  end up with less precise code

#ACTUALLY recording cordinates several times may not be bad.
# THOUGH only proper way to know is to test both/ try writing both
def record_mouse(exit_key = "esc"):
    print()