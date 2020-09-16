n_v = ''
x = 0
m = 0
maior = 0
count1 = 0
for p in range(1,5):
    nome = input('Digite o nome da {}º pessoa: '.format(p))
    i = int(input('Digite a idade: '))
    s = input('Coloque M para aculino e F para feminino: ')
    x += i
    m = x / 4
    if i < 20 and s == 'f':
        count1 += 1
    if p == 1 and s == 'm':
        maior = i
        n_v = nome
        if i > maior:
          maior = i
          n_v = nome
print('O nome do mais velho é : {}'.format(n_v))
print('Média de idade: {}'.format(m))
print('Mulheres com menos de 20 anos: {}'.format(count1))
