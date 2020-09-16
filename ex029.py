km = int(input('Digite a velocidade que o carro estava: '))
if km <= 80:
    print('Sem problemas, você não tem multa!')
else:
    m = (km - 80)* 7.00
    print(' Você ultrapassou o limite permitido!\n O valor da ulta será de R${:.2f}'.format(m))