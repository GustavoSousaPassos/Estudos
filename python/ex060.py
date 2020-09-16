num = int(input('Digite um número: '))
fat = 1
x = 1
while fat <= num:
    x *= fat
    fat += 1
print('fatorial: {}'.format(x))
