count = 0
p1 = 1
p2 = 1
num = 0
print(p1)
while count <= 9:
    num = p2
    p2 = p1 + p2
    p1 = num
    print(p2)
    count += 1
