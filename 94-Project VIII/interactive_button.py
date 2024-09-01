from tkinter import *

window = Tk()

# create a function

def greeting_msg():
    greeting_a = Label(text = "What is your name",font= "Arial 14 bold", fg = "orange", bg ="blue" )
    greeting_a.pack()
    greeting_b = Label(text = "How are you?",font= "Arial 14 bold", fg = "black", bg ="red" )
    greeting_b.pack()

btn = Button(text="Click Me", font= "Arial 14 bold", fg = "white", bg ="green", command = greeting_msg)
btn.pack()

window.mainloop()