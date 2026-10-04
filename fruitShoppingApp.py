# tkinter is a graphical library of python
from tkinter import *

# creating the window of the app
window = Tk()

# define the size of the window
window.geometry("800x600")

# give a title of the app
window.title("Fruit Shopping App!")

# give colour to the window
window.config(background = "#FF1919")

# creates and displays the heading on the screen
heading = Label(window, text = "Fruit Shopping App!", font = ("Lexend", 30, "bold"), background = "#FF1919", fg = "white")
heading.place(x = 215, y = 50)

# creates and displays the fruit label on the screen
fruit = Label(window, text = "Select Fruits:", font = ("Arial", 15), background = "#FF1919", fg = "white")
fruit.place(x = 50, y = 130)

# creates a spinbox of fruits
fruits = Spinbox(window, values = ("Apple", "Orange", "Pear", "Banana", "Grapes", "Melon", "Pineeapple", "Papaya", "Dragonfruit", "Jackfruit", "Guava"))
fruits.place(x = 180, y = 137)

# creates and displays the fruit label on the screen
quantityLabel = Label(window, text = "Select Quantity:", font = ("Arial", 15), background = "#FF1919", fg = "white")
quantityLabel.place(x = 50, y = 170)

# creates a spinbox of fruits
quantity = Spinbox(window, from_ =0, to = 20)
quantity.place(x = 180, y = 177)

# ensures it stays on screen
window.mainloop()