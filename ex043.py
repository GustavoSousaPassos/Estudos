from math import pow
p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura; '))
imc = p / pow(a,2)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc <= 25:
    print('Peso normal!')
elif imc <= 30:
    print('Acima do peso!')
elif imc <= 40:
    print('Sobrepeso!')
else:
    print('Você está obeso!')
