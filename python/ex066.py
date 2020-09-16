soma = num = count = 0
while True:
    num = int(input('digite um número'))
    if num == 999:
        break
    count += 1
    soma += num
print(f'Números digitados: {count} \nSoma total: {soma}')