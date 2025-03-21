# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # TC = O(N) | SC = O(N)
        res = 0
        if not root: return res # not necessary
        def dfs(curr, maxV):
            nonlocal res
            if curr.val >= maxV:
                res += 1
                maxV = curr.val
            if curr.left: dfs(curr.left, maxV)
            if curr.right: dfs(curr.right, maxV)

        dfs(root, root.val)
        return res
