import win32con
import win32api
from time import sleep
from keymouse.vkcodes import VK_CODE

#todo figure out how to get characters for number keys like $

def press_keys(*keys):
    for i in keys:
        #http://timgolden.me.uk/pywin32-docs/win32api__keybd_event_meth.html
        win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)
        sleep(0.05)
        win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), win32con.KEYEVENTF_KEYUP, 0)


def press_keys_and_hold(*keys):
    for i in keys:
        win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)
        sleep(0.05)

def press_keys_hold_and_release(*keys):
    for i in keys:
        win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)
        sleep(0.05)
    for i in keys:
        win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), win32con.KEYEVENTF_KEYUP, 0)
        sleep(0.05)

def release(*keys):
    for i in keys:
        win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), win32con.KEYEVENTF_KEYUP, 0)
        sleep(0.05)

