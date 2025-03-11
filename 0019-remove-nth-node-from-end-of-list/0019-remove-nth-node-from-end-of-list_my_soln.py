# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m, count, curr = 0, 0, head
        while curr:
            m += 1
            curr = curr.next
        
        pos = m - n
        if pos == 0: head = head.next
        else:
            curr = head
            while curr:
                count += 1
                if pos == count:
                    curr.next = curr.next.next
                    break
                curr = curr.next
        
        return head
