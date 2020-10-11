cont = int(input('Digite um número: '))
count = 0
for c in range(1,cont):
  if c % cont == 0:
    print(c)
    count += 1
  else:
    print(c)

print(f'O número {cont} foi divisivel {count} vezes')

