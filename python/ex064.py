count = 0
soma = 0
num = int(input('Digite um número: '))
while num != 999:
    count += 1
    soma += num
    num = int(input('Digite outro número: '))
print('Quantidade de números digitados: {}'.format(count))
print('Soma total entre os valores digitados: {}'.format(soma))
