import time
import pyautogui
import tkinter as tk
from tkinter import *

def screenshot() :
    
    name = int(round(time.time() * 1000))
    name = 'D:/vs code/my_folder/python/py_projects/Mini_Projects/screenshots data\\{}.png'.format(name)
    # time.sleep(5) # 5 seconds after initialization ss os taken
    # img = pyautogui.screenshot('ss1.png')
    img = pyautogui.screenshot(name)
    img.show()
    
window  = Tk()
frame = Frame(window)
frame.pack()

btn = Button(frame, text= "Take Screenshot", command= screenshot)
btn.pack(side = tk.LEFT)

close = Button(frame, text= "QUIT", command= quit )
close.pack(side = tk.LEFT)

window.mainloop()