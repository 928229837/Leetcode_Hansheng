
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        d = {}
        res = ListNode(0)
        for i in lists:
            while i:
                d[i.val] = d[i.val] + 1 if d.get(i.val) else 1
                i = i.next
        cur = res
        for v, l in sorted(d.items()):
            for i in range(l):
                cur.next = ListNode(v)
                cur = cur.next

        return res.next