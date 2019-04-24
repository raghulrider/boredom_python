# User data input Entry

from tkinter import Tk

root = Tk()

get_username = Label(root, text = "Username >>", bg ="orange")
get_password = Label(root, text = "Password >>", bg = "orange")

username = Entry(root, bg = "grey")
password = Entry(root, bg = "grey")

get_username.grid(row = 0, column =0)
get_password.grid(row = 1, column = 0)

username.grid(row = 0, column = 1)
password.grid(row = 1, column = 1)
c = Checkbutton(root,text = "Keep me signed in", bg = "orange")
c.grid(columnspan = 2)
root.mainloop() 