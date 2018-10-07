# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def ser(node):
            if node is None:
                res.append('#')
            else:
                res.append(str(node.val))
                ser(node.left)
                ser(node.right)

        ser(root)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())

        def des():
            val = next(vals)
            if val == '#':
                return None
            else:
                new_node = TreeNode(val)
                new_node.left = des()
                new_node.right = des()
                return new_node

        return des()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


a = "1 2 # # 3 4 # # 5 # #"

asd = Codec().deserialize(a)

print(Codec().serialize(asd))