n1 = float(input('Digite sua primeira nota: '))
n2  = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Reprovado')
elif m <= 6.9:
    print('Recuperação')
else:
    print('Aprovado!')
