class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestLength = 0
        currentLength = 0
        currentStart = 0
        hashTable = {}

        for i in range(len(s)):
            if s[i] in hashTable and hashTable[s[i]] >= currentStart:
                if currentLength > longestLength:
                    longestLength = currentLength
                currentLength = i - hashTable[s[i]]
                currentStart = hashTable[s[i]] + 1
            else:
                currentLength += 1
            hashTable[s[i]] = i
        if currentLength > longestLength:
            return currentLength
        return longestLength


if __name__ == "__main__":

    test = Solution()
    a = ['abcabcbb', 'bbbbbb', 'pwwkew']
    for i in range(len(a)):
        print(a[i], test.lengthOfLongestSubstring(a[i]))





