# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # TC = O(N) | SC = O(N)
        if not root: return []
        res = []
        def dfs(curr, depth):
            if len(res) == depth: res.append([])
            res[depth].append(curr.val)
            if curr.left: dfs(curr.left, depth + 1)
            if curr.right: dfs(curr.right, depth + 1)

        dfs(root, 0)
        return res