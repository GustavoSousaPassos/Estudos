#CORES NO PYTHON
# Será usado o codigo ansi para o terminal
#
#      \003[style;text;back m]
#           * style:
#               - 0: none
#               - 1: bold
#               - 4: underline
#               - 7: inverte as ordens das cores
#
#           * text:
#               - 30: White
#               - 31: Red
#               - 32: green
#               - 33: yellow
#               - 34: blue
#               - 35: Magenta, entre violeta e roxo
#               - 36: Ciano; verde-água, azul_piscina; mistura de luzes azuis e verdes
#               - 37: cinza
#
#           * background:
#               - O mesmo para texto, porém começa do 40
print('\033[1;36m Olá Mundo!\033[m')
a = 3
b = 8
print('Digite um um número entre \033[1;31;m{} \033[me \033[36m{}\033[m'.format(a,b))
nome = 'Gustavo'
print('É um prazer conhece-lo {}{}{}!!!'.format('\033[1;7;30m',nome,'\033[m'))
