# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkValid(self, curr, minVal, maxVal):
        if not curr: return True
        if minVal < curr.val < maxVal:
            return self.checkValid(curr.left, minVal, curr.val) and self.checkValid(curr.right, curr.val, maxVal)
        else: return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkValid(root, -float('inf'), float('inf'))
