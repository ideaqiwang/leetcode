## 113. Path Sum III
### Description
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:  
```
           5
         /   \
        4     8
       /    /   \ 
      11   13    4 
     /  \       /  \
    7    2     5    1
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22  
Output: [[5,4,11,2],[5,8,4,5]]  
Explanation: There are two paths whose sum equals targetSum:  
5 + 4 + 11 + 2 = 22  
5 + 8 + 4 + 5 = 22  

### Solution
* DFS

```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        self.res = []
        self.traverse(root, [], 0, targetSum)
        return self.res
        
    def traverse(self, root, path, curSum, targetSum):
        if not root.left and not root.right:
            if curSum+root.val == targetSum:
                self.res.append(path+[root.val])
            return
        
        path.append(root.val)
        if root.left:
            self.traverse(root.left, path, curSum+root.val, targetSum)
        if root.right:
            self.traverse(root.right, path, curSum+root.val, targetSum)
        path.pop()
```
