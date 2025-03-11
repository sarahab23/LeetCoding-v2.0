# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # T O(n) M O(n) - memory is linear operation because it's recursion, it takes n recursive
        # calls
        if not head: return head
        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None
        return newHead