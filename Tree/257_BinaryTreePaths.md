## 257. Binary Tree Paths

### Description

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:  
```
     1  
   /   \  
  2     3  
   \  
    5
```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

### Solution

* Preorder traversal
* When visit a leaf node, add the path to the result list
* Time Complexity: O(n)

```python
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        self.res = []
        self.dfs(root, '')
        return self.res
        
    def dfs(self, root, path):
        if not root:
            return

        path += str(root.val)
        if not root.left and not root.right:
            self.res.append(path)
        else:
            path += '->'
            self.dfs(root.left, path)
            self.dfs(root.right, path)
```