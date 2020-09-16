# desenvolva um programa que leia a progressão e a razaõ de uma PA(progressão aritimeticac), mostre os 10 primeiros termos
num = int(input('Digite o primeiro termo da progressão aritimetica: '))
r = int(input('Digte a razão:'))
v = num + r
#print(num)

for c in range(num,9):
    print(v)
    v += r