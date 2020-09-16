val_i = 0
i = 0
res_i = ''
t_num = (int(input('Digite um número:')),
         int(input('Digite outro número:')),
         int(input('Digite mias um número: ')),
         int(input('Digite o ultimo número: ')))
print('Os números pares foram encontrados na poisção: ', end=' ')
for c in range(len(t_num)):
    if t_num[c] == 9:
        i += 1
    if t_num[c] == 3:
        res_i = 'Sim, na posição'
        val_i = c + 1
        break
    else:
        res_i = 'Não'
        val_i = ''
    if t_num[c] % 2 == 0:
        print(c+1, end=' ')
print(f'\nO número nove foi encontrado {i} vezes \n O valor três foi encontrado? {res_i} {val_i} \nhá valores pares nas posições')