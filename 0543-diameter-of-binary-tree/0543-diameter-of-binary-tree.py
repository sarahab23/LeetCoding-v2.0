# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # TC = O(n) SC = O(logn) -> Space complexity will be the recursion depth, which is at most the height (h) of the tree. Balanced Tre = logN & Skewed Tree = N
        res = 0

        def getDepth(root):
            if not root: return 0

            left = getDepth(root.left) if root.left else 0
            right = getDepth(root.right) if root.right else 0

            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right)
        
        getDepth(root)
        return res
