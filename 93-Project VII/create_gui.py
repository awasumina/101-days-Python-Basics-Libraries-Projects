from tkinter import *

# create an instance
window = Tk()

greeting = Label(text = "Hello everyone")
greeting.pack()

# without main loop the new window wont open and we cant define requirements inside it
window.mainloop()
