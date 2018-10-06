# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

import math


def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    b = list(range(n))
    if n < 2:
        return 0
    s = [1] * n
    s[0] = s[1] = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        print(i, b)
        print(i*i, ':', n, ':', i, 'int', (n - i * i - 1) / i + 1, int((n - i * i - 1) / i + 1))
        if s[i] == 1:
            print('!!!', i, s)
            s[i * i:n:i] = [0] * int((n - i * i - 1) / i + 1)
            print('$$$', i, s)

    return sum(s)


a = countPrimes(50)
print(a)
