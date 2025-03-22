# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        def findK(curr):
            nonlocal count
            if curr.left:
                res = findK(curr.left)
                if res != None: return res
            count -= 1
            if count == 0: return curr.val
            if curr.right:
                res = findK(curr.right)
                if res != None: return res

        return findK(root)
