from tkinter import *

root = Tk()
root.geometry("200x100+100+100")

lb1 = Label(root, text="Login")
lb2 = Label(root, text="Senha")

ed1 = Entry(root)
ed2 = Entry(root)

bt1 = Button(root, text="Confimar")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
bt1.grid(row=2, column=1)

root.mainloop()