'''
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
'''

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
        if not root:
            return ""
        
        res = ""
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node:
                res += str(node.val)+","
                q.append(node.left)
                q.append(node.right)
            else:
                res += "#,"
        return res[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nums = data.split(",")
        root = TreeNode(nums[0])
        q = [root]
        isLeftChild = True
        index = 0

        for i in range(1, len(nums)):
            if nums[i] != "#":
                node = TreeNode(int(nums[i]))
                if isLeftChild:
                    q[index].left = node
                else:
                    q[index].right = node
                q.append(node)
    
            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))