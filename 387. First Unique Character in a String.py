# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


class Solution:
    def firstUniqChar(self, s):
        ans = len(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            c_s = s.find(c)
            c_r = s.rfind(c)
            if c_s == c_r and c_s != -1:
                ans = min(ans, c_s)
        return ans if ans < len(s) else -1