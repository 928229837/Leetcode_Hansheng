# 1 2 3 5 7    0 holes
# 0 4 6        1 holes
# 8            2 holes

def hole(num):
    res = 0
    for n in num:
        n = int(n)
        if n in {1,2,3,5}:
            continue
        elif n in {0,4,6}:
            res += 1
        elif n == 8:
            res += 2
    return res


print(hole("1288"))