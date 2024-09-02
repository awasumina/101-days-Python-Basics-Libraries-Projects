from tkinter import *

window = Tk()
# place() aren't responsive

frame = Frame(master = window, width = 200, height=200)
frame.pack()

# create label widgets
label_a = Label(master = frame, text="I am at (0,0)", bg ="green", fg="yellow")
label_a.place(x= 0, y =0)

label_b = Label(master = frame, text="I am at (50,50)", bg ="red", fg="white")
label_b.place(x= 50, y =50)

label_c = Label(master = frame, text="I am at (100,125)", bg ="yellow", fg="black")
label_c.place(x= 100, y = 125)

window.mainloop()
