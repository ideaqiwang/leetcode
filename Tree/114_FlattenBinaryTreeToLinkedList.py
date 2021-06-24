'''
114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
           1                1
          /  \               \ 
        2     5        ==>    2  
       / \     \               \ 
      3   4     6               3
                                 \ 
                                  4
                                   \ 
                                    5
                                     \ 
                                      6
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1 - DFS
    def flatten1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
    
    def dfs(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
        leftTail = self.dfs(root.left)
        rightTail = self.dfs(root.right)
        
        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            root.left = None
        return rightTail if rightTail else leftTail
        
    # Solution 2 - Iterative with a stack
    def flatten2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.p = TreeNode()
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                node.left = None
  
            self.p.right = node
            self.p = self.p.right

    # Solution 3 - Iterative in place
    def flatten3(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
                                                #  1
        node = root                             #   \
        while node:                             #    2
            if node.left:                       #   / \ 
                rightMost = node.left           #  3   4
                while rightMost.right:          #       \ 
                    rightMost = rightMost.right #        5
                                                #         \ 
                rightMost.right = node.right    #          6
                node.right = node.left
                node.left = None
            # Move no to the right side of the tree
            node = node.right