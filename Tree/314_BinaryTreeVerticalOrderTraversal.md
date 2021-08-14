## 314. Binary Tree Vertical Order Traversal

### Description

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Example 1:  
```
         3
       /   \
      9    20
          /  \
         15   7 
```
Input: root = [3,9,20,null,null,15,7]  
Output: [[9],[3,15],[20],[7]]  

### Solution

* BFS traverse the given tree level by level with a relative offset to root. Go left -> descrease 1. Go right -> increase 1

```python
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        depth2list = defaultdict(list)
        
        q = deque([(root, 0)])
        while q:
            node, depth = q.popleft()
            depth2list[depth].append(node.val)
            if node.left:
                q.append((node.left, depth-1))
            if node.right:
                q.append((node.right, depth+1))

        return [depth2list[x] for x in sorted(depth2list.keys())]
```
