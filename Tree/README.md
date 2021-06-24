# Binary Tree Traversal
* pre-order traversal
* in-order traversal
* post-order traversal



### Recursive Traversal


### Iterative Traversal

* pre-order traversal
```python
    def preorder(root: TreeNode):
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            print(node.val)
```
  
* in-order traversal
```python
    def inorder(root: TreeNode)
        node = root
        stack = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            print(node.val)
            node = node.right
```