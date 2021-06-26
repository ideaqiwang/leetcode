'''
270. Closest Binary Search Tree Value

Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

Example 1:
       7
      / \ 
     3   15
        /  \        
       9   20
Input: root = [7, 3, 15, null, null, 9, 20], target = 4
Output: 3
'''

class Solution:
    # Use BST property to do binary search
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.minDiff = sys.maxsize
        self.dfs(root, target)
        return self.res
        
    def dfs(self, root, target):
        if not root:
            return
        diff = abs(root.val - target)
        if diff < self.minDiff:
            self.minDiff = diff
            self.res = root.val
        if root.val >= target:    
            self.dfs(root.left, target)
        else:
            self.dfs(root.right, target)