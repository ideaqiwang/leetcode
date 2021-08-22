## 199. Binary Tree Right Side View

### Description

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:  
```
          1        <===  1
        /   \      
       2     3     <===  3
        \     \
         5     4   <===  4
```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

### Solution
* BFS
```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        res = []
        
        while q:
            node = None
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(node.val)
        return res
```
