# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def getDepth(root):
            nonlocal res
            if not root: return 0
            left = getDepth(root.left) if root.left else 0
            right = getDepth(root.right) if root.right else 0
            if abs(right - left) > 1: res = False
            return 1 + max(left, right)
        
        getDepth(root)
        return res