n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite mais um número inteiro: '))
if n1 > n2 and n1 > n3 and n2 > n3:
    print('O maior número é {}'.format(n1))
    print('enquanto o menor será {}'.format(n3))
elif n1 > n2 and n1 > n3 and n3 > n2:
    print('O maior número será {}'.format(n1))
    print('O menor número será {}'.format(n2))
if n2 > n1 and n2 > n3 and n1 > n3:
    print('O número maior será {}'.format(n2))
    print('O número menor será {}'.format(n3))
elif n2 > n1 and n2 > n3 and n3 > n1:
    print('O maior número será {}'.format(n2))
    print('O menor número será {}'.format(n1))
if n3 > n1 and n3 > n2 and n1 > n2:
    print('O número maoir será {}'.format(n3))
    print('O número menor será {}'.format(n2))
elif n3 > n1 and n3 > n2 and n2 > n1:
    print('O maior número será {}'.format(n3))
    print('O menor número será {}'.format(n1))