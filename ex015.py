al = int(input('Digite o número de dias que o carro foi alugado: \033[1;30;35m'))
km = float(input('Digite o quantidade de quilometros rodados: '))
vt = (al*60) + (km*0.15)
print('O valor a ser pago será: R${}{:.2f}{}.'.format('\033[0;32m',vt,'\033[m'))
