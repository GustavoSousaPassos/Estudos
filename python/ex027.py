nome = str(input('Digite seu nome completo: '))
l = nome.split()
print(' Primeiro nome: {}'.format(l[0]))
print('Sobrenome: {}'.format(l[len(l)-1]))
