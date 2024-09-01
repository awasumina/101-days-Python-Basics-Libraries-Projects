from tkinter import *

window = Tk() 

frame_a = Frame()
label_a = Label(master = frame_a, text =" Learn python doing projects")
label_a.pack()

frame_b =  Frame()
label_b = Label(master= frame_b, text =" I am a programmer")
label_b.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()