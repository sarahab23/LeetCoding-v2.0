"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        store = {}
        copyHead = Node(head.val, None, None)
        store[head] = copyHead
        curr, copyCurr = head.next, copyHead 
        while curr:
            dummy = Node(curr.val, None, None)
            copyCurr.next = dummy
            copyCurr = copyCurr.next
            store[curr] = copyCurr
            curr = curr.next
        
        curr = head
        while curr:
            if not curr.random: store[curr].random = None 
            else: store[curr].random = store[curr.random]
            curr = curr.next
        
        return copyHead
