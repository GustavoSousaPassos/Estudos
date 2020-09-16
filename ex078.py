lista = []

for c in range(0,5):
    lista.append(int(input('Put a number:')))
max_num = max(lista)
min_num = min(lista)
print(f'The maximum number is {max_num}, and is in positions ', end="")
for pos, d in enumerate(lista[0:]):
    if d == max_num:
        print(pos+1)
print(f'The minimum number is {min_num}, and is in positions ', end='')
for pos2, e in enumerate(lista[0:]):
    if e == min_num:
        print(pos2+1)