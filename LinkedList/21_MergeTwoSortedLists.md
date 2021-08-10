## 21. Merge Two Sorted Lists

### Description

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:  
1 -> 2 -> 4  
1 -> 3 -> 5  
1 -> 1 -> 2 -> 3 -> 4 -> 5  
Input: l1 = [1,2,4], l2 = [1,3,5]  
Output: [1,1,2,3,4,5]  

### Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p. next = l2
                l2 = l2.next
            p = p.next

        p.next = l1 if l1 else l2
        return dummy.next
```