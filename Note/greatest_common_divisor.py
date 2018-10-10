
def recursion():
    def hcfnaive(a, b):
        if (b == 0):
            return a
        else:
            return hcfnaive(b, a % b)
    print("The gcd of 60 and 48 is : ", end="")
    print(hcfnaive(60, 48))

def loops():
    def computeGCD(x, y):
        if x > y:
            small = y
        else:
            small = x
        for i in range(1, small + 1):
            if ((x % i == 0) and (y % i == 0)):
                gcd = i
        return gcd
    print("The gcd of 60 and 48 is : ", end="")
    print(computeGCD(60, 48))

def Euclidean():
    def computeGCD(x, y):
        while (y):
            x, y = y, x % y

        return x
    print("The gcd of 60 and 48 is : ", end="")
    print(computeGCD(60, 48))


def useMath():
    import math
    print("The gcd of 60 and 48 is : ", end="")
    print(math.gcd(60, 48))


if __name__ == "__main__":
    i = 1
    if i == 1:   recursion()
    elif i == 2: loops()
    elif i == 3: Euclidean()
    elif i == 4: useMath()
