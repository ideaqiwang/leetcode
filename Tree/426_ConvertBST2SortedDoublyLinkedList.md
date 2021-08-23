## 426. Convert Binary Search Tree to Sorted Doubly Linked List

### Description

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

Example 1:
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

### Solution
* Traverse BST iteratively with a stack

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        cur = dummy = Node(0)
        node, tail = root, None
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            node.left = cur
            cur.right = node
            cur = cur.right
            
            tail = node
            node = node.right
        
        head = dummy.right
        head.left = tail
        tail.right = head
        return head
```
