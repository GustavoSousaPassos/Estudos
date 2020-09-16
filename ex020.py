from random import shuffle
x = str(input('Digite o nome do aluno'))
y = str(input('Digite outro nome'))
z = str(input('Digite mais um aluno'))
l = [x, y, z]
shuffle(l)
print('A ordem de alunos : {}'.format(l))