pro_cheap = ''
pro_value = pro_sum = count = pro_v_cheap = opt = point = 0
while True:
    pro_name = str(input('Enter with name of product: '))
    pro_value = float(input('Enter with the value: '))
    point += 1
    if pro_value > 100:
        count += 1
    if point == 1 or pro_value < pro_v_cheap:
        pro_v_cheap = pro_value
        pro_cheap = pro_name
    pro_sum += pro_value
    opt = int(input('There are more products? \n[0] Yes \n[1] No'))
    if opt == 1:
        break
print(f'Total: {pro_sum :.2f} \nThere are {count} expensive products \nCheap product: {pro_cheap}')