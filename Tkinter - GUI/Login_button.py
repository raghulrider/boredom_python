#login button
from tkinter import *

root = Tk()
def save_credentials():
    print("Username:", username)
    print("Password:", password)

frame = Frame(root)
login = Button(frame,text = "Login", bg ="orange" , command = save_credentials)

get_username = Label(root, text = "Username >>", bg ="orange")
get_password = Label(root, text = "Password >>", bg = "orange")

username = Entry(root, bg = "grey")
password = Entry(root, bg = "grey")



#c = Checkbutton(root,text = "Keep me signed in", bg = "orange")
#c.grid(columnspan = 2)

login.pack()
frame.pack(side = LEFT)
root.mainloop() 