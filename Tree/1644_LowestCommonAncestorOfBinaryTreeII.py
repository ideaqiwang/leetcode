'''
1644. Lowest Common Ancestor of a Binary Tree II

Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

Example 1:
            3
          /   \ 
        5       1
       / \     / \ 
      6   2   0   8
         / \ 
        7   4
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        foundP, foundQ, ancestor = self.dfs(root, p, q)
        if foundP and foundQ:
            return ancestor
        return None
    
    def dfs(self, root, p, q):
        if not root:
            return False, False, None
      
        lp, lq, left = self.dfs(root.left, p, q)
        rp, rq, right = self.dfs(root.right, p, q)
        
        foundP = (lp or rp or root == p)
        foundQ = (lq or rq or root == q)
        
        if root == p or root == q:
            return foundP, foundQ, root
        
        if left and right:
            return True, True, root
        if left:
            return foundP, foundQ, left
        if right:
            return foundP, foundQ, right
        return foundP, foundQ, None