count = 0
a = 2019
p = 7
for c in range(1,8):
    ano = int(input('Qual o ano de nascimento da {}º pessoa? ano: '.format(c)))
    x = a - ano
    if x < 18:
        count += 1
if count == 0:
    print('Todas as pessoas atingiram a maioridade!')
else:
    print('Existe ainda {} pessoas que não atingiram a maioridade!'.format(count))
