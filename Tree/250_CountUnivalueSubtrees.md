## 250. Count Univalue Subtrees
### Description
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

Example 1:
Input: root = [5,1,5,5,5,null,5]
Output: 4

### Solution
* DFS

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.traverse(root)
        return self.count
        
    def traverse(self, root):
        if not root:
            return True

        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        if left and right and (not root.left or root.val == root.left.val) and \
        (not root.right or root.right.val == root.val):
            self.count += 1
            return True
        return False
```
