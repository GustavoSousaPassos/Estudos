from random import choice
j = ['pedra','papel', 'tesoura']
r = int(input('Vamos começar a jogar jokenpo escolha entre: \n[1]pedra \n[2]papel \n[3]tesoura'))
a = choice(j)
if a == r:
    print('Empate')
elif r == 1:
    if a == j[2]:
        print('Você perdeu')
    else:
        print('Você ganhou!')
elif r == 2:
    if a == j[1]:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
elif r == 3:
    if a == j[1]:
        print('Você perdeu')
    else:
        print('Você ganhou!')
