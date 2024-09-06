# pip install virtualenv -> allows us to create a virtual environment
# pip install pyautogui

import time
import pyautogui

def screenshot() :
    
    name = int(round(time.time() * 1000))
    name = 'D:/vs code/my_folder/python/py_projects/Mini_Projects/screenshots data\\{}.png'.format(name)
    time.sleep(5) # 5 seconds after initialization ss os taken
    # img = pyautogui.screenshot('ss1.png')
    img = pyautogui.screenshot(name)
    img.show()
    
screenshot()