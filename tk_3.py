# Aula 10 (comando fill)
'''

    fill -> Mostra qual o sentido que o widget se expande:
        x -> Para a horizontal
        y -> Para a vertical

'''

from tkinter import *

# Create and configured the window
root = Tk()
root.geometry("500x500+100+100")
root["bg"] = "lightblue"

# Create the widgets

lb1 = Label(root, text="Hello world!")
lb2 = Label(root, text="Hello world!", background="green")
lb3 = Label(root, text="Hello world!", background="orange")

# Configure the widgets

lb1.pack(side=TOP,fill=BOTH, expand=0)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP,fill=BOTH, expand=1)

root.mainloop()