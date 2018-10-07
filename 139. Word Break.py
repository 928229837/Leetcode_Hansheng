class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        cache = {""}
        for i in range(len(s)):
            if s[:i] in cache:
                for word in wordDict:
                    cache.add(s[:i]+word)
        return s in cache


s = "leetcode"
w = ["leet", "code"]
print(Solution().wordBreak(s, w))