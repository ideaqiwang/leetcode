'''
@Description https://leetcode.com/problems/binary-tree-level-order-traversal/
@IDEA
  Use a queue to traverse the tree level by level
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = collections.deque([root])
        while q:
            level = []
            for i in range(len(q)): # In python we can do this. In other languages, we need to save the length of q to a variable
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
