count = 0
cont = 0
while cont == 0:
    num = int(input('Digite o primeiro número da progressão aritimetica: '))
    r = int(input('Digite a razão: '))
    while count <= 9:
        num += r
        print(num)
        count += 1
    opc = input('Gstaria de continuar com outro termo? [S/N]: ')
    if opc == 's':
        count = 0
    else:
        break