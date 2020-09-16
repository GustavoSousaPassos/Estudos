num = int(input('Digite um número qualquer: '))
opc = int(input('Qual conversão de base você deseja? \n[1]Binario \n[2]Octal \n[3]hexadecimal \nopção:'))
if opc == 1:
    r1 = bin(num)
    print('A conversão de {} para binario é igaul à {}'.format(num, r1[2:]))
elif opc == 2:
    r2 = oct(num)
    print('A conversão de {} para octal é igual à {}'.format(num,r2[2:]))
else:
    r3 = hex(num)
    print('A conversão de {} para hexadecimal é igual a {}'.format(num, r3 [2:].upper()))