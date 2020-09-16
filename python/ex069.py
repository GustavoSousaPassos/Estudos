opc = count = count_m = count_w = age = genre = 0
while True:
    age = int(input('Enter with your age'))
    genre = int(input('Enter with your genre: \n[1]Man \n[2]Woman'))
    if age >= 18:
        count += 1
    if genre == 1:
        count_m += 1
    if age < 20 and genre == 2:
        count_w += 1
    opc = int(input('To add more people? \n[1] Yes \n[2] Not \noption: '))
    if opc == 2:
        print(f'People with majority age: {count} \nMen: {count_m} \nWomen with less 20 years old: {count_w}')
        break