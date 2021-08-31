## 297. Serialize and Deserialize Binary Tree

### Description

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

### Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
    
        q = deque([root])
        bfsOrder = []
        while q:
            node = q.popleft()
            bfsOrder.append(str(node.val) if node else '#')
            if node:
                q.append(node.left)
                q.append(node.right)
        return ','.join(bfsOrder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        bfsOrder = [TreeNode(int(value)) if value != '#' else None for value in data.split(',') ]
        root = bfsOrder[0]
        q = [root]
        slow, fast = 0, 1
        
        while slow < len(q):
            node = q[slow]
            slow += 1
            node.left = bfsOrder[fast]
            node.right = bfsOrder[fast+1]
            fast += 2
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```
