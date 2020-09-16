a = int(input('Digite um número'))
u = a // 1 % 10
d = a // 10 % 10
c = a // 100 % 10
m = a // 1000 % 10
print(' Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(u,d,c,m))