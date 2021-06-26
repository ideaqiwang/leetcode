'''
87. Remove Node in Binary Search Tree

Given a root of Binary Search Tree with unique value for each node.
Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing.
You should keep the tree still a binary search tree after removal.

Example 1:
Input:

Tree = {5,3,6,2,4}
value = 3
Output:

{5,2,6,#,4} or {5,4,6,2}
Explanation:

Given binary search tree:
    5
   / \ 
  3   6
 / \ 
2   4
Remove 3, you can either return:
    5
   / \ 
  2   6
   \ 
    4
or
    5
   / \ 
  4   6
 /
2
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if not root:
            return None
        head = TreeNode(0)
        head.left = root
        parent, node = head, root

        # Find the target node
        while node:
            if node.val == value:
                break
            parent = node
            # Go to the left subtree
            if node.val > value:
                node = node.left
            else:
                node = node.right
        
        if not node:
            return head.left

        # Find the new node to replace the current node
        # If no right subtree, use the left node to replace
        if not node.right:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
        # If right node doesn't have left subtree,
        # which means it's the min node in the right subtree
        elif not node.right.left:
            if parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
            node.right.left = node.left
        else:
            # The right subtree is quiet large, have to find the min node of it
            # The left most node is the min node
            parent = node.right
            p = parent.left
            while p.left:
                parent = p
                p = p.left
            
            node.val = p.val
            parent.left = p.right

        return head.left
