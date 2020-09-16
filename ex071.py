count50 = count20 = count10 = count1 = pr = 0
pr = int(input('Enter with money that need: '))
while True:
    if pr == 0:
       break
    else:
        while pr >= 50:
           count50 += 1
           pr = pr - 50
        while pr >= 20:
           count20 += 1
           pr = pr - 20
        while pr >= 10:
           count10 += 1
           pr = pr - 10
        while pr >= 1:
           count1 += 1
           pr = pr - 1
        break
print(f'50\'s bills : {count50} \n 20\'s bills: {count20} \n10\'s bills: {count10} \n1\'s bills: {count1}')
