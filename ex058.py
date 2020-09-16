from random import randint
a = randint(1,10)
num = int(input('Digite um número: '))
while num != a:
    num = int(input('Digite novamente: '))
print('Você acertou!')