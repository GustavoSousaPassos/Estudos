p = ('Pão', 1.00, 'Detergente', 1.50, 'Leite', 3.00)


print('---------------------------------')
print('        Listagem de preços       ')
print('---------------------------------')

for pos,c in enumerate(p[0::2]):
    pro = c
    pre = pos+1
    print(f'{pro} ................. R${pre:.2f}')
print('----------------------------------')
