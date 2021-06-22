'''
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example:
        5
       / \
      1   4
          /\
         3  6
Input: root = [5,1,4,null,null,3,6]
Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Inorder tranvse a BST would visite nodes in acsend order 
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, -math.inf, math.inf)
        
    def dfs(self, root, low, high):
        if not root:
            return True
        if not (low < root.val < high):
            return False
        return self.dfs(root.left, low, root.val) and self.dfs(root.right, root.val, high)