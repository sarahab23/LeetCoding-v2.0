# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None: return head

        curr = head.next
        prev = head
        prev.next = None

        while curr.next != None:
            head = curr.next
            curr.next = prev
            prev = curr
            curr = head

        head = curr
        curr.next = prev
        
        return head
        