'''
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k,
return the kth (1-indexed) smallest element in the tree.

Example 1:
           3
          / \  
         1   4
          \ 
           2     
Input: root = [3,1,4,null,2], k = 3
Output: 3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1 - Iterative traversal
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = root
        stack = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right

    # Solution 2 - Recursive traversal
    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        self.index = 1
        self.ans = None
        self.dfs(root, k)
        return self.ans
        
    def dfs(self, root, k):
        if not root:
            return
        self.dfs(root.left, k)
        if self.index == k:
            self.ans = root.val
        self.index += 1
        self.dfs(root.right, k)

'''
Follow up:
What if search very often, how to optimize?
'''
class Solution2:
    '''
    Use a hash map to store the number of childrens of each node.
    Then do a quick select.
    '''
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.nodeOfChildren = {}
        self.countNodes(root)
        return self.quickSelect(root, k)
        
    def countNodes(self, root):
        if not root:
            return 0
        leftCount = self.countNodes(root.left)
        rightCount = self.countNodes(root.right)
        self.nodeOfChildren[root] = leftCount+rightCount+1
        return self.nodeOfChildren[root]

    def quickSelect(self, root, k):
        if not root:
            return -1

        leftCount = 0
        if root.left:
            leftCount = self.nodeOfChildren[root.left]
        if leftCount >= k:
            return self.quickSelect(root.left, k)
        if leftCount+1 == k: # need to take the current root into account
            return root.val
        return self.quickSelect(root.right, k-leftCount-1)

