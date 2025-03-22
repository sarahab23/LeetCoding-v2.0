# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, curr):
        if curr.left: self.dfs(curr.left)
        self.li.append(curr.val)
        if curr.right: self.dfs(curr.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.li = []
        self.dfs(root)
        return self.li[k-1]