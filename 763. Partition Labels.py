class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        last_index = {}
        for i in range(len(S)):
            last_index[S[i]] = i
        start, end = 0, 0
        for i in range(len(S)):
            end = max(end, last_index[S[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res