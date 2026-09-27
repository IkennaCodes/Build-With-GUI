# tkinter is a graphical library of python
from tkinter import *

# creating the window of the app
window = Tk()

# define the size of the window
window.geometry("800x600")

# give a title of the app
window.title("School Forum!")

# give colour to the window
window.config(background = "#848484")

# creates and displays the heading on the screen
heading = Label(window, text = "School Personal Details Formum", font = ("Lexend", 30, "bold"), background = "#848484", fg = "white")
heading.place(x = 120, y = 50)

# creates and displays the name label on the screen
name = Label(window, text = "Name:", font = ("Arial", 15), background = "#848484", fg = "white")
name.place(x = 50, y = 130)

# create an entry box for name
nameEntry = Entry(window, width = 30, font = ("Arial", 15), background = "#848484", fg = "white")
nameEntry.place(x = 120, y = 133)

# creates and displays the age label on the screen
age = Label(window, text = "Age:", font = ("Arial", 15), background = "#848484", fg = "white")
age.place(x = 50, y = 180)

# create an entry box for age
ageEntry = Entry(window, width = 30, font = ("Arial", 15), background = "#848484", fg = "white")
ageEntry.place(x = 120, y = 183)

# creates and displays the year label on the screen
year = Label(window, text = "Year:", font = ("Arial", 15), background = "#848484", fg = "white")
year.place(x = 50, y = 240)

# create an entry box for year
year = Entry(window, width = 30, font = ("Arial", 15), background = "#848484", fg = "white")
year.place(x = 120, y = 243)

# creates and displays the school name label on the screen
schoolName = Label(window, text = "School:", font = ("Arial", 15), background = "#848484", fg = "white")
schoolName.place(x = 50, y = 300)

# create an entry box for schoolname
schoolName = Entry(window, width = 30, font = ("Arial", 15), background = "#848484", fg = "white")
schoolName.place(x = 120, y = 303)

# creates and displays the country label on the screen
country = Label(window, text = "Country:", font = ("Arial", 15), background = "#848484", fg = "white")
country.place(x = 50, y = 360)

# create an entry box for country
country = Entry(window, width = 30, font = ("Arial", 15), background = "#848484", fg = "white")
country.place(x = 120, y = 363)

# creates and displays the country label on the screen
classs = Label(window, text = "Class:", font = ("Arial", 15), background = "#848484", fg = "white")
classs.place(x = 50, y = 420)

# create an entry box for country
classs = Entry(window, width = 30, font = ("Arial", 15), background = "#848484", fg = "white")
classs.place(x = 120, y = 423)



# ensures it stays on screen
window.mainloop()