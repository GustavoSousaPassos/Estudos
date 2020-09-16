maior = 0
menor = 0
for p in range(1,5+1):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O peso maior: {}'.format(maior))
print('O peso menor: {}'.format(menor))
