'''
257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:
      1
     / \ 
    2   3
     \ 
      5
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.allPaths = []
        self.dfs(root, '')
        return self.allPaths
    
    def dfs(self, root, path):
        path += str(root.val)
        if not root.left and not root.right:
            self.allPaths.append(path)
        else:
            path += "->"
            if root.left:
                self.dfs(root.left, path)
            if root.right:
                self.dfs(root.right, path)
