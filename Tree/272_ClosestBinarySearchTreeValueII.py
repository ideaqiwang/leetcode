'''
272. Closest Binary Search Tree Value II

Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example 1:
Example 1:
       4
      / \ 
     2   5
    /  \        
   1   3
Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        self.ans = deque()
        self.inorder(root, target, k)
        return self.ans
    
    def inorder(self, root, target, k):
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            self.ans.append(node.val)
            if len(self.ans) > k:
                if abs(self.ans[-1]-target) < abs(self.ans[0]-target):
                    self.ans.popleft()
                else:
                    self.ans.pop()
            node = node.right