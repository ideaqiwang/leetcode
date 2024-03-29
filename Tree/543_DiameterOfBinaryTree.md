## 543. Diameter of Binary Tree

### Description
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
```
        1
      /   \
     2     3
   /  \
  4    5   
```
Input: root = [1,2,3,4,5]  
Output: 3  
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].  

### Solution

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, root):
        if not root:
            return 0
        
        left_length = self.dfs(root.left)
        right_length = self.dfs(root.right)
        self.diameter = max(self.diameter, left_length+right_length)
        
        return max(left_length, right_length)+1
```
