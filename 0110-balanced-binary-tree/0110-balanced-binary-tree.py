# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(root):
            if not root: return 0
            left = getDepth(root.left) if root.left else 0
            right = getDepth(root.right) if root.right else 0
            if abs(right - left) > 1 or left == -1 or right == -1:
                return -1
            return 1 + max(left, right)
        
        return getDepth(root) != -1