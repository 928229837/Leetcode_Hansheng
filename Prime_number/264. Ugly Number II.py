# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors
# only include 2, 3, 5.

# Example:
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence
# of the first 10 ugly numbers.


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [0] * n
        i1 = i2 = i3 = -1
        x = v1 = v2 = v3 = 1
        for i in range(n):
            x = min(v1, v2, v3)
            ugly[i] = x
            if x == v1:
                i1 += 1
                v1 = ugly[i1] * 2
            if x == v2:
                i2 += 1
                v2 = ugly[i2] * 3
            if x == v3:
                i3 += 1
                v3 = ugly[i3] * 5
        return ugly[-1]


