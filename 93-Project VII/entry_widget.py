from tkinter import *

window = Tk()

# create Entry Widget -> accepts only single line text
# entry widget -> allows user to input
# entry = Entry(fg = "green", bg = "aqua", width = 50)
# entry.pack()

label = Label(text ="User Name")
entry = Entry()
label.pack()
entry.pack()

# retrieving text with .get()

# deleting text with. delete()

# inserting text with .insert()

# TEXT WIDGET -> we can take multiple lines of codes

text_box = Text()
text_box.pack()

window.mainloop()
