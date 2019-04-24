#India for fun

from tkinter import Tk

root = Tk()

top = Label(root, text = "\n\n", bg = "orange")
middle = Label(root, text = "\n Indian Flag \n", bg = "white")
bottom = Label(root, text = "\n\n", bg = "green")

top.pack(fill = X)
middle.pack(fill = X)
bottom.pack(fill = X)

root.mainloop()