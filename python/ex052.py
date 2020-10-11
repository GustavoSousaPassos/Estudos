cont = int(input('Digite um número: '))
count = 0
for c in range(1,cont+1):
  if cont % c == 0:
    print(f'\033[1;32m{c}\033[m', end=" ")
    count += 1
  else:
    print(f'\033[1;31m{c}\033[m', end=" ")

print(f'\nO número {cont} foi divisivel {count} vez(es)')

if count > 1:
  print('Por isso ele não é primo!')
else:
  print('Por isso ele é primo')

