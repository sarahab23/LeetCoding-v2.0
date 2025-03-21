# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        q = deque([(root, -float('inf'))])
        while q:
            for i in range(len(q)):
                node, maxV = q.popleft()
                if node.val >= maxV:
                    res += 1
                    maxV = node.val
                if node.left: q.append((node.left, maxV))
                if node.right: q.append((node.right, maxV))

        return res   
