from tkinter import *                                               #importando todas as funções presentes no modulo

def bt_click():
    print('Hello, world!')                                          # Criando uma função pára altera a inforação contida no label atribuido na variavél "lb"
    lb["text"] = 'Funcionou!'
    bt["bg"] = "gray"

root = Tk()                                                         # Criando uma instacia e atribuindo a variavél janela (TK é a calsse padrão para criação de uma janela

#lb = Label(root, text="Hello, World!").pack()    #trabalhando com o gerenciador pack, cria-se um label vinculado com a a variavel


lb = Label(root, text="Hello, World!")                              # Criando um label qure irá ficar no container "root". Essa instancia é atribuida a uma variavel "lb"
lb.place(x= 100, y= 100)                                            # Essa instancia será exibida por meio do gerenciador de layout place, que mostrará a x de distancia da margem do monitor e y ao topo do mesmo

bt = Button(root, width=20, text="Clique aqui!", command=bt_click)  # Criando um botão na janela principal, contendo uma função caso clicado
bt.place(x=200,y=200)                                               # Determinando a posição do botão

root.title("Teste Tkinter")                                         # Determinando um titulo no cabeçalho

root.config(background ="darkgreen")                                # Determinando a cor de fundo
#root["bg"] = "purple"

# DETERMINANDO O TAMANHO DA PAGINA PRINCIPAL
root.geometry("800x300+100+100")                                    # Largura x Altura + espaçamento a esquerda + espaçamento do topo
                                                                    # Caso alguns atributos não sejam colocados, e estabelecido o tamanho padrão e colocado aleatoriamente na tela
root.mainloop()
