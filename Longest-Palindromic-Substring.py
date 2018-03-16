# Given a strings, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
# Example:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example:
# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ''
        hash_s = []
        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = i



        pass


if __name__ == "__main__":
    s = 'babad'
    a = Solution().longestPalindrome(s)
    print(a)


