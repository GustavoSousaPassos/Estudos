num = 0
while True:
    i = 0
    num = int(input('Digite um número: '))
    if num < 0:
        break
    while i <= 10:
        print(f'{num} x {i} = {num*i}')
        i += 1
