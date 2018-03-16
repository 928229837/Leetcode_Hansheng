import timeit


def binary(x):
    i = 1
    j = x
    while(i <= j):
        m = i + (j - i)//2
        if m > x / m:
            j = m - 1
        else:
            i = m + 1
    return j

def newton(a):
    x = a
    while x*x > a:
        x = (x + a//x )//2
    return x

s = timeit.default_timer()
print(binary(9**33))
print((timeit.default_timer()-s))

s = timeit.default_timer()
print('\n',newton(9**33))
print((timeit.default_timer()-s))