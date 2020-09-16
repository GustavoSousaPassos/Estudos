from random import randint
num = int(input('Escreva um número de 0 a 5'))
v = randint(0,5)
print('Você venceu!' if num == v else'O computador venceu!')