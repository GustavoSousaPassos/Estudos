from tkinter import *

'''
    Grenciador de layout grid:
        
        - Intuitivo
        - Facil manutenção
        - Mais usado
        - Mais legivél

        Propriedades:
            row - linha
            column - coluna
            sticky - seelhante ao anchor, vincula um sentido para o widget
                - N(north), S(south), E(east), W(west)
                - NW, NS, SW, SE
            columnspan and rowspan - mescla as colunas/linhas proximas
                - O número colocado determina a quantidade a ser mesclada 
'''

# Create and configure the window

root = Tk()
root.geometry("500x500+100+100")

# Create the widgets

lb1 = Label(root,text="Hello world!", background="green")
lb2 = Label(root,text="Hello world again!", background="blue")

lb1.grid(row=500, column=500)
lb2.grid(row=500, column=500)

root.mainloop()
