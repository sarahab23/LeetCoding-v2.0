# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # TC = O(N) | SC = O(N)
        if not root: return 0
        res = 1
        q = collections.deque([(root, root.val)])
        while q: 
            for i in range(len(q)):
                node, maxV = q.popleft()
                if node.left:
                    if node.left.val >= maxV:
                        res += 1
                        q.append((node.left, node.left.val))
                    else: q.append((node.left, maxV))
                if node.right:
                    if node.right.val >= maxV:
                        res += 1
                        q.append((node.right, node.right.val))
                    else: q.append((node.right, maxV))
        
        return res
            
