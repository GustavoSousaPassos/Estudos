# Aula 8 (Extração de dados usando o comando get()) e aula 9 (Entrada e processamento  de dados) juntas

from tkinter import *

#Criando as funções:

def btn_onclick():
    '''root.geometry('500x500+200+200')'''
    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric():
        n1 = int(ed1.get())
        n2 = int(ed2.get())
        lb["text"] = n1 + n2
    else:
        lb["text"] = "Os valores digitados são inválidos"

#Criando a página:

root = Tk()
root.geometry("500x300+200+100")

#Colocando os widgets:

ed1 = Entry(root)
ed1.place(x=100,y=100)

ed2 = Entry(root)
ed2.place(x=100,y=130)

btn = Button(root, width="20", text="Ok", command=btn_onclick)
btn.place(x=100,y=150)

lb = Label(root, text="Label")
lb.place(x=100,y=200)

root.mainloop()