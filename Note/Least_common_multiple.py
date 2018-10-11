def lcm_brute_force(x, y):
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


def faster(a, b):
    product = a*b
    while b:
        a, b = b, a % b
    return product//a  # a is gcd


GCD = lambda a, b: (GCD(b, a % b) if a % b else b)

# a, b = 9, 67
a, b= 2, 3
print(a, b, GCD(a,b))
print(a, b, faster(a, b))
print((a*b)//GCD(a, b))

# num1 = 9
# num2 = 67
# print(num1, "and", num2, "least common multi is:", lcm_brute_force(num1, num2))