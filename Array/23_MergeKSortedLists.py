'''
23. Merge K Sored Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

ListNode.__lt__ = lambda x, y : (x.val < y.val)

class Solution1:
    # Use a Heap
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        p = dummy = ListNode()
        hq = []
 
        for head in lists:
            if head:
                heapq.heappush(hq, head)
        
        while hq:
            node = heapq.heappop(hq)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(hq, node.next)
        return dummy.next

class Solution2:
    # Divide and Conquer
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.mergeRangeLists(lists, 0, len(lists)-1)
    
    def mergeRangeLists(self, lists, start, end):
        if start == end:
            return lists[start]
        m = (start+end) // 2
        left = self.mergeRangeLists(lists, start, m)
        right = self.mergeRangeLists(lists, m+1, end)
        return self.merge2Lists(left, right)

    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next