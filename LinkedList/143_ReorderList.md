## 143. Reorder List

### Description

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln  
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …  
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:  
Input: head = [1,2,3,4]  
Output: [1,4,2,3]  

### Solution
* Find the middle point
* Reverse the second half of the list
* Merge the first half and the second half

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        midNode = self.findMiddle(head)
        head2 = midNode.next
        midNode.next = None
        
        head2 = self.reverseList(head2)
        return self.mergeTwoLists(head, head2)
        
    def findMiddle(self, head):
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseList(self, head):
        if not head:
            return None

        newHead = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = newHead
            newHead = cur
            cur = nxt
        return newHead
    
    def mergeTwoLists(self, head1, head2):
        dummy = ListNode()
        cur = dummy
        p1, p2 = head1, head2
        i = 0
        while p1 and p2:
            if i % 2 == 0:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
            i += 1
        cur.next = p1 if p1 else p2
        return dummy.next
```

