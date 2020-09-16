count = 0
num = int(input('Digite um núero qualquer: '))
for c in range(1, num+1):
    d = num % c
    if d == 0:
        count += 1
if count == 2:
    print('{} é um número primo!'.format(num))
else:
    print('Esse número não é primo!')
