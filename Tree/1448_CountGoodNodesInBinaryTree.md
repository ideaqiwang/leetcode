## 1448. Count Good Nodes in Binary Tree
### Description
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
```
         3
       /   \
      1     4
     /     / \
    3     1   5   
```
Input: root = [3,1,4,3,null,1,5]  
Output: 4  
Explanation: Nodes in blue are good.  
Root Node (3) is always a good node.  
Node 4 -> (3,4) is the maximum value in the path starting from the root.  
Node 5 -> (3,4,5) is the maximum value in the path  
Node 3 -> (3,1,3) is the maximum value in the path.  

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
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.traverse(root, -sys.maxsize)
        return self.count
        
    def traverse(self, root, maxValue):
        if not root:
            return
    
        if root.val >= maxValue:
            self.count += 1
        
        maxValue = max(maxValue, root.val)
        self.traverse(root.left, maxValue)
        self.traverse(root.right, maxValue)
```
