# tkinter is a graphical library of python
from tkinter import *

# creating the window of the app
window = Tk()

# define the size of the window
window.geometry("800x600")

# give a title of the app
window.title("Menu Bar!")

# give colour to the window
window.config(background = "#FE5ECE")

menuBar = Menu(window)

#creates a menu in the window
window.config(menu = menuBar)

# creates file menu
file_menu = Menu(menuBar, tearoff = 0)

# adds sections into it
menuBar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New Text File", command = None)
file_menu.add_command(label = "New File", command = None)
file_menu.add_command(label = "New Window", command = None)
file_menu.add_command(label = "New Window with Profile", command = None)
file_menu.add_separator()
file_menu.add_command(label = "Open File", command = None)
file_menu.add_command(label = "Close Window", command = window.destroy)

edit_menu = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = None)
edit_menu.add_command(label = "Redo", command = None)
edit_menu.add_separator()
edit_menu.add_command(label = "Cut", command = None)
edit_menu.add_command(label = "Copy", command = None)
edit_menu.add_command(label = "Paste", command = None)
edit_menu.add_separator()
edit_menu.add_command(label = "Find", command = None)
edit_menu.add_command(label = "Replace", command = None)
edit_menu.add_separator()
edit_menu.add_command(label = "Find in Files", command = None)
edit_menu.add_command(label = "Replace in Files", command = None)
edit_menu.add_separator()
edit_menu.add_command(label = "Toggle Line Comment", command = None)
edit_menu.add_command(label = "Toggle Block Comment", command = None)
edit_menu.add_command(label = "Emmet: Expand Abbriviation", command = None)


# ensures it stays on screen
window.mainloop()