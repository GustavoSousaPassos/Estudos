from random import randint
num = opc = soma = 0
ch = res = ''
while True:
    ch_m = randint(0,10)
    num = int(input('Digite um número: '))
    opc = int(input('Digite uma opção: \n[1]Par \n[2]Impar \nopção: '))
    soma = ch_m + num
    print(f'Você tirou {num} e a maquina {ch_m} dando no total {soma}')
    if opc == 1:
        ch = 'par'
    else:
        ch = 'impar'
    if soma % 2 == 0:
        res = 'par'
    else:
        res = 'impar'
    if ch == res:
        print('Você ACERTOU!')
    else:
        print('Você perdeu, fim de jogo!')
        break