a = float(input('Digite o medida de um lado A do triângulo: '))
b = float(input('Digite o lado B agora: '))
c = float(input('Agora digite o lado C: '))
r1 = b + c
r2 = c + a
r3 = a + b
if a < r1 and b < r2 and c < r3:
    print('É possivel forma um triângulo com essas medidas!')
    if a == b and b == c:
        print('Esse triângulo é equilátero')
    elif a == b and b != c or c == a and a != b:
        print('Esse triângulo é isóceles')
    else:
        print('Esse triângulo é escalaneno')
else:
    print('Não é possivel forma um triângulo com essas medidas!')