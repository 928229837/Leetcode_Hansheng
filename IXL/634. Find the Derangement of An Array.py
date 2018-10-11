# In combinatorial mathematics, a derangement is a permutation of the
#  elements of a set, such that no element appears in its original
# position.
#
# There's originally an array consisting of n integers from 1 to n in
# ascending order, you need to find the number of derangement it can
# generate.
#
# Also, since the answer may be very large, you should return the
# output mod 109 + 7.
#
# Example 1:
# Input: 3
# Output: 2
# Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
# Note:
# n is in the range of [1, 106].


class Solution:
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in {1, 0}:
            return 0
        elif n == 2:
            return 1
        first, second = 0, 1
        for i in range(n-2):
            first, second = second, (first+second)*(i+2)%(1000000007)
            print(i+3, first, second)
        return second

Solution().findDerangement(12)