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
        serialized = []

        def serial(root):
            if not root:
                serialized.append('#')
            else:
                serialized.append(str(root.val))
                serial(root.left)
                serial(root.right)

        serial(root)
        return ' '.join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = iter(data.split())
        print(data)
        def deserial():
            nodeval = next(data)
            if nodeval == '#':
                return None
            else:
                newNode = TreeNode(nodeval)
                newNode.left = deserial()
                newNode.right = deserial()
                return newNode

        return deserial()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

a = "1 2 # # 3 4 # # 5 # #"

asd = Codec().deserialize(a)

print(Codec().serialize(asd))