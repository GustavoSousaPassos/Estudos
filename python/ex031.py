d = float(input('Digite a distacia da viajem em kilometros:'))
if d <= 200:
    p1 = d * 0.50
    print('O valor da sua passagem será de R$ {:.2f}'.format(p1))
else:
    p2 = d* 0.45
    print('O valor de sua passagem será de R$ {:.2f}'.format(p2))
print('Boa viagem!')