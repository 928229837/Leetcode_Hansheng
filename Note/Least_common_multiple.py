def lcm(x, y):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


num1 = 9
num2 = 67

print(num1, "and", num2, "least common multi is:", lcm(num1, num2))