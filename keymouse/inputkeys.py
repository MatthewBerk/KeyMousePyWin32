import win32con
import win32api
from time import sleep
from keymouse.vkcodes import VK_CODE
from ctypes import windll

#todo figure out how to get characters for number keys like $

#use if
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
    press_keys_and_hold(keys)
    release(keys)

def release(*keys):
    for i in keys:
        win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), win32con.KEYEVENTF_KEYUP, 0)
        sleep(0.05)

#Use when want to send uppercase letters or special characters like $
def shift_press_keys(*keys):
    i=1
    #todo

