# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        prev, carry = head, 0
        while l1 and l2:
            summ = l1.val + l2.val + carry
            sumD, carry = summ % 10, summ // 10
            dummy = ListNode(sumD)
            prev.next = dummy
            prev, l1, l2 = dummy, l1.next, l2.next
        
        while l1:
            summ = l1.val + carry
            sumD, carry = summ % 10, summ // 10
            dummy = ListNode(sumD)
            prev.next = dummy
            prev, l1 = dummy, l1.next
        
        while l2:
            summ = l2.val + carry
            sumD, carry = summ % 10, summ // 10
            dummy = ListNode(sumD)
            prev.next = dummy
            prev, l2 = dummy, l2.next
        
        if carry > 0:
            dummy = ListNode(carry)
            prev.next = dummy
        
        return head.next