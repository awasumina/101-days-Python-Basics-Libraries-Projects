import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.title("Dice Roll")
window.geometry("500x360")

# def roll_dice():
#     dice1 = random.randint(1, 6)
#     label = tk.Label(window, text = dice1).pack()

# btn = tk.Button(window, text="Click", command = roll_dice)
# btn.pack()

dice = ["one.jpg","two.jpg","three.jpg", "four.png","five.png","six.png"]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window, image = image1)
label2 = tk.Label(window, image = image2)

label1.place(x = 40, y = 100)
label2.place(x = 300, y = 100)

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = image2)
    label2.image = image2

button = tk.Button(window, text = "ROLL", bg = "green", fg = "white", font = "Time 14 bold")
button.place(x = 200, y =0)

window.mainloop()