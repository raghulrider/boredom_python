#using frames and buttons

from tkinter import Tk

root  = Tk()

tstframe1 = Frame(root)
tstframe2 = Frame(root)

label = Label(root, text = "Test using buttons and frames")

button1 = Button(tstframe1, text = "I'm at the Top :)")
button2 = Button(tstframe2, text = "I'm at the Bottom :(")

button1.pack()
button2.pack()

label.pack()

tstframe1.pack(side = TOP)
tstframe2.pack(side = BOTTOM)

root.mainloop()