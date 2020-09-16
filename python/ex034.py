s = float(input('Digite o valor de seu salário, sem o uso de pontuação: '))
if s <= 1250:
    a1 = s + (s * 0.15)
    print('Seu salário teve um aumento, agora o valor total será de R$ {:.2f}'.format(a1))
else:
    a2 = s + (s * 0.10)
    print('Seu salário sofreu um aumento, seu valor agopra será de R$ {:.2f}'.format(a2))
print('Aproveite o aumento!')