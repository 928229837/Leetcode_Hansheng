class Solution(object):
    def partitionLabels(self, S):
        intervals = {}
        res = []
        """save first apear and last appear index of each character"""
        for i, c in enumerate(S):
            intervals[c] = (intervals.get(c, (i, i))[0], i)

        cur = intervals[S[0]]
        for c in S:
            """check whether or not first appear is in the cur range"""
        if intervals[c][0] > cur[1]:
            res.append(cur[1] - cur[0] + 1)
            cur = intervals[c]

    """first appear in cur range but last not, update last of cur range"""
    elif intervals[c][1] > cur[1]:
    cur = (cur[0], intervals[c][1])


res.append(cur[1] - cur[0] + 1)

return res