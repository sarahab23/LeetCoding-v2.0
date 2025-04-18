# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q, res = deque([root]), []
        while q:
            levelNodes = []
            for i in range(len(q)):
                curr = q.popleft()
                levelNodes.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            res.append(levelNodes)
        
        return res
