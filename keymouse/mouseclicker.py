from time import sleep
import win32api
import win32con


def click_at(x, y, times=1, delay=0):
    #http://timgolden.me.uk/pywin32-docs/win32api__SetCursorPos_meth.html
    win32api.SetCursorPos((x,y))
    while (times > 0):
        times -= 1
        sleep(delay)
        #http://timgolden.me.uk/pywin32-docs/win32api__mouse_event_meth.html
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)# todo Doesn't seem to need coordinates, look into more
        sleep(0.05)  # test to see if need.
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def click_at_current_pos(times=1, delay=0):
    #http://timgolden.me.uk/pywin32-docs/win32api__GetCursorPos_meth.html
    x,y = win32api.GetCursorPos()
    while (times > 0):
        times -= 1
        sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        sleep(0.05)  # test to see if need.
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

#For if want to drag an item/application to a new spot
def click_and_move(x1,y1,x2,y2, times=1,delayrepeat= 0,delaydrag=0.5):
    while(times>0):
        times -= 1
        sleep(delayrepeat)
        win32api.SetCursorPos((x1, y1))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1, 0, 0)
        sleep(delaydrag)
        win32api.SetCursorPos((x2, y2))
        sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x2, y2, 0, 0)