count = 0
soma = 0
media = 0
num = int(input('Digite um número'))
maior = num
menor = num
opc = int(input('Gostaria de continuar? [0] Sim [1] Não \nopção: '))
while opc == 0:
    num = int(input('Digite outro número: '))
    soma += num
    count += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    opc = int(input('Gostaria de continuar? [0] Sim [1] Não \nopção: '))
media = soma / count
print('A media total dos números digitados: {}'.format(media))
print('O número maior: {}'.format(maior))
print('O número menor: {}'.format(menor))
