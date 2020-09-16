count = 0
a = 2019
p = 7
for c in range(1,8):
    ano = int(input('Digite a idade da {}º pessoa: '.format(c)))
    x = a - ano
    if x < 18:
        count += 1
if count == 0:
    print('Todas as pessoas atingiram a maioridade!')
else:
    print('Existe ainda {} pessoas que não atingiram a maioridade!'.format(count))
