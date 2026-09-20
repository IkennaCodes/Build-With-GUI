


# tkinter is a graphical library of pythoon
from tkinter import *

# creating the window of the app
window = Tk()

# define the size of the window
window.geometry("800x600")

# give a title of the app
window.title("First TKinter App!")

# give colour to the window
window.config(background = "#FEC95E")

# creates and displays the heading on the screen
heading = Label(window, text = "Personal Details Form", font = ("Lexend", 30, "bold"), background = "#FEC95E", fg = "white")
heading.place(x = 200, y = 50)

# creates and displays the name label on the screen
name = Label(window, text = "Name:", font = ("Arial", 15), background = "#FEC95E", fg = "white")
name.place(x = 50, y = 130)

# create an entry box for name
nameEntry = Entry(window, width = 30, font = ("Arial", 15), background = "#FDDD9E", fg = "#B89900")
nameEntry.place(x = 120, y = 133)

# creates and displays the age label on the screen
age = Label(window, text = "Age:", font = ("Arial", 15), background = "#FEC95E", fg = "white")
age.place(x = 50, y = 180)

# create an entry box for age
ageEntry = Entry(window, width = 30, font = ("Arial", 15), background = "#FED176", fg = "black")
ageEntry.place(x = 120, y = 183)


# ensures it stays on screen
window.mainloop()