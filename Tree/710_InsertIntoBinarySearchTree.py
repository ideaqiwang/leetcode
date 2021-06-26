'''
710. Insert Into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:
       4                                4      
      / \                             /   \      
     2   7                   =>      2     7     
    / \                             / \   /      
   1   3                           1   3 5     
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
'''

class Solution:
    # Solution 1 - Recurtion
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    # Solution 2 - Iteration
    def insertIntoBST2(self, root: TreeNode, val: int) -> TreeNode:
        newNode = TreeNode(val)
        if not root:
            return newNode
        
        node = root
        while node != newNode:
            # Search in the right subtree
            if node.val < val:
                if not node.right:
                    node.right = newNode
                node = node.right
            else:
                if not node.left:
                    node.left = newNode
                node = node.left
        return root