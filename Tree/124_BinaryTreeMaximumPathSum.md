## 124. Binary Tree Maximum Path Sum

### Description

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

Example 1:  
```
             -10  
            /   \  
           9    20  
               /  \
              15   7 
```
Input: root = [-10,9,20,null,null,15,7]  
Output: 42  
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.  

### Solution
* Time Complexity: O(n)

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -inf
        self.pathSum(root)
        return self.maxSum

    def pathSum(self, root):
        if not root:
            return 0
        
        leftSum = max(self.pathSum(root.left), 0)
        rightSum = max(self.pathSum(root.right), 0)
        self.maxSum = max(self.maxSum, leftSum+root.val+rightSum)
        
        return root.val+max(leftSum, rightSum)
```