from tkinter import *

# create an instance
window = Tk()

# create label widget
label = Label(text = "Hello everyone", fg = "black", bg="orange", width = 20, height= 20)
label.pack()

# without main loop the new window wont open and we cant define requirements inside it
window.mainloop()
