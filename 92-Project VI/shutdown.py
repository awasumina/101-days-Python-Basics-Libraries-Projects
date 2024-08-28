from tkinter import *
import os

window = Tk()
window.title("ShutDown App")
window.geometry("500x500") 
window.config(bg= "lightblue")

def restart():
    os.system('shutdown /r /t 1')
    
def time_restart():
    os.system("shutdown /r /t 20")
    
def logout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t 1")

r_button = Button(window, text="Restart", font =("Time New Roman", 20, "bold"), relief= RAISED, cursor= "plus", command= restart)
r_button.place(x = 150, y = 60, height= 50, width = 200)

rt_button = Button(window, text="Restart Time", font =("Time New Roman", 20, "bold"), relief= RAISED, cursor= "plus", command= time_restart)
rt_button.place(x = 150, y = 170, height= 50, width = 200)

lg_button = Button(window, text="Log Out", font =("Time New Roman", 20, "bold"), relief= RAISED, cursor= "plus", command= logout)
lg_button.place(x = 150, y = 270, height= 50, width = 200)

st_button = Button(window, text="Shut Down", font =("Time New Roman", 20, "bold"), relief= RAISED, cursor= "plus", command= shutdown)
st_button.place(x = 150, y = 370, height= 50, width = 200)

window.mainloop()