from math import cos,radians,sin,tan
b = int(input('Digite o valor do ângulo desejadado: '))
s = sin(radians(b))
c = cos(radians(b))
t = tan(radians(b))
print(' O valor da seno será : {:.2f}\n O valor do coseno será {:.2f}\n O valor da Tangente será {:.2f}'.format(s,c,t))
