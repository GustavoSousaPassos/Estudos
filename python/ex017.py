from math import sqrt, pow
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))
c = sqrt(pow(a,2) + pow(b,2))
print('O valor da hipotenusa ira medir {:.2f}'.format(c))
