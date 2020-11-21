from pyautogui import *
import pyautogui
import time
import keyboard
import numpy
import win32api, win32con

#NOTES
#ALWAYS run game in fullscreen 1920x1080 (maybe a diff resolution later?)
#Need to find position for each (0,0)
#Might need to switch all click (x,y) to image recognition if the repositioning doesnt work like I want it to (Aka dont ever have to touch it :D)

time.sleep(3)

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def leftdown (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)

def leftup (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con_MOUSEEVENTF_LEFTODNW,0,0)
    


def scroll_down (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, -1, 0) #Scroll one down

def sleep (x,y): #Random Number between X and Y
    time.sleep(np.random.uniform(x,y))

def Recenter_Screen():
    time.sleep (3) #maybe? probably lol
    click (0,0) #Click RSS
    sleep (1,3)
    click (0,0) #Click Left Person (Wait)
    sleep (5,6)
    click (0,0) #Click X on RSS
    sleep (1,3)
    click (0,0) #Click Home
    sleep (5,6)
    scroll_down (0,0) #Need to find optimal position for scroll

def Plant():
    #Check to see if land is open if so continue, if not go to Harvest. (Greyscale check? Color Check? Image recognition?)
    click (0,0) #Click bottom left plot
    sleep(1,2)
    leftdown (0,0) #Need to hold wheat icon and drag it around
    pyautogui.moveTo(0, 0, 0) # moves mouse to X,Y in Z amount of seconds (Will have to do this like 6 times with sleeps inbetween randommized (like 0.2-0.8 seconds?))

def Harvest():
    click (0,0) #Click bottom left wheat plot
    sleep(1,2)
    leftdown (0,0) #Holding the sickle
    pyautogui.moveTo(0, 0, 0) #gotta do this alot : (

def Sell():
    #If first slot is empty, click on box -> click wheat -> advertise? -> repeat for each slot (sell at 1 or 10?)
    #If not empty, go back to reposition
    click (0,0) #Click RSS


