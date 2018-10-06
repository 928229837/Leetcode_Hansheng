# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

"""
My solution
"""

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        res, level = [], [root]
        while level:
            res.append(level[-1].val)
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return res


# Solution 1: Recursive, combine right and left: 5 lines, 56 ms
#
# Compute the right view of both right and left left subtree, then combine them. For very unbalanced trees, this can be O(n^2), though.

def rightSideView(self, root):
    if not root:
        return []
    right = self.rightSideView(root.right)
    left = self.rightSideView(root.left)
    return [root.val] + right + left[len(right):]
# Solution 2: Recursive, first come first serve: 9 lines, 48 ms
#
# DFS-traverse the tree right-to-left, add values to the view whenever we first reach a new record depth. This is O(n).

def rightSideView(self, root):
    def collect(node, depth):
        if node:
            if depth == len(view):
                view.append(node.val)
            collect(node.right, depth+1)
            collect(node.left, depth+1)
    view = []
    collect(root, 0)
    return view
# Solution 3: Iterative, level-by-level: 7 lines, 48 ms

# Traverse the tree level by level and add the last value of each level to the view. This is O(n).

def rightSideView(self, root):
    view = []
    if root:
        level = [root]
        while level:
            view += level[-1].val,
            level = [kid for node in level for kid in (node.left, node.right) if kid]
    return view