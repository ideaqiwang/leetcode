'''
61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
1 -> 2 -> 3 -> 4 -> 5
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
0 -> 1 -> 2
Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Return the length and the last node
    def length(self, head):
        count = 0
        pre = p = head
        while p:
            count += 1
            pre = p
            p = p.next
        return count, pre

    def rotateRight(self, head, k):
        if not head:
            return head
        n, last = self.length(head)
        k %= n
        if k == 0:
            return head
        index = n - k
        pre = newHead = head
        for _ in range(index):
            pre = newHead
            newHead = newHead.next
        pre.next = None
        last.next = head
        return newHead
