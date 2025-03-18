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
            left, right = getDepth(root.left), getDepth(root.right)
            if left == -1 or right == -1 or abs(right - left) > 1:
                return -1
            return 1 + max(left, right)
        
        return getDepth(root) != -1