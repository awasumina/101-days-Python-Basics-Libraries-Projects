# controlling Application Layout with Geometry Managers
# Geometry Managers -> .pack(), .grid(), .place()

from tkinter import *

window = Tk()

# defaults center
# frame_a = Frame(master=window, width = 150, height= 150, bg = "blue")
# frame_a.pack() 

# frame_b = Frame(master=window, width = 100, height= 100, bg = "red")
# frame_b.pack()

# frame_c = Frame(master=window, width = 50, height= 50, bg = "green")
# frame_c.pack()

# frame_d = Frame(master=window, width = 10, height= 10, bg = "yellow")
# frame_d.pack()

# ----------------- size and X and Y parameters are defined
# frame_a = Frame(master=window, width = 150, height= 150, bg = "blue")
# frame_a.pack(fill=X) # defaults center

# frame_b = Frame(master=window, width = 100, height= 100, bg = "red")
# frame_b.pack(fill=X)

# frame_c = Frame(master=window, width = 50, height= 50, bg = "green")
# frame_c.pack(fill=Y, side=LEFT)

# frame_d = Frame(master=window, width = 10, height= 10, bg = "yellow")
# frame_d.pack(fill=Y, side = LEFT)


# ------------------ in both direction
frame_a = Frame(master=window, width = 150, height= 150, bg = "blue")
frame_a.pack(fill = BOTH, side= RIGHT, expand=True) # defaults center

frame_b = Frame(master=window, width = 100, height= 100, bg = "red")
frame_b.pack(fill = BOTH, side= RIGHT, expand=True)

frame_c = Frame(master=window, width = 50, height= 50, bg = "green")
frame_c.pack(fill = BOTH, side= RIGHT, expand=True)

frame_d = Frame(master=window, width = 10, height= 10, bg = "yellow")
frame_d.pack(fill = BOTH, side= RIGHT, expand=True)

window.mainloop()