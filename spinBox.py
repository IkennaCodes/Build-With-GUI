# tkinter is a graphical library of python
from tkinter import *

# creating the window of the app
window = Tk()

# define the size of the window
window.geometry("800x600")

# give a title of the app
window.title("Make your PROJECT!")

# give colour to the window
window.config(background = "#848484")

# creates and displays the heading on the screen
heading = Label(window, text = "Spinbox", font = ("Lexend", 30, "bold"), background = "#FD8E8E", fg = "white")
heading.place(x = 300, y = 30)

spinbox1 = Spinbox(window, values = ("Yellow", "Green", "Red", "Blue", "Orange", "Pink", "Purple", "Black", "Brown"))
spinbox1.place(x = 120, y = 150)

spinbox2 = Spinbox(window, from_ =0, to = 10)
spinbox2.place(x = 120, y = 200)

# ensures it stays on screen
window.mainloop()