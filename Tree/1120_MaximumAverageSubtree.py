'''
1120. Maximum Average Subtree

Given the root of a binary tree, find the maximum average value of any subtree of that tree.
(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

Example 1:
   4
  / \
 3   1
/ \
0 2
Input: [4, 3, 1, 0, 2]
Output: 2.00000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Postorder traversal
    1. Calculate sum and the number of a subtree
    '''
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.maxAvg = -sys.maxsize
        self.dfs(root)
        return self.maxAvg
        
    def dfs(self, root):
        if not root:
            return 0, 0
        
        tl, cl = self.dfs(root.left)
        tr, cr = self.dfs(root.right)
        total = tl + tr + root.val
        count = cl + cr + 1

        self.maxAvg = max(self.maxAvg, total/count)
        return total, count