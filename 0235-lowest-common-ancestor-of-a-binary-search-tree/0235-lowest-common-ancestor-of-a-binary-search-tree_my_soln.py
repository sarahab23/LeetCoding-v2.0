# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prevElts = []
        self.pList, self.qList = [], []

    def findLCA(self, pList, qList):
        h = min(len(pList), len(qList))
        for l in range(h):
            if pList[l] == qList[l]: res = pList[l]
            else: break
        return res

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        self.prevElts.append(root)
        if root.val == p.val:
            self.pList = list(self.prevElts)
        if root.val == q.val:
            self.qList = list(self.prevElts)

        if self.pList and self.qList:
            return self.findLCA(self.pList, self.qList)

        if root.left: 
            res = self.lowestCommonAncestor(root.left, p, q)
            if res: return res
        if root.right: 
            res = self.lowestCommonAncestor(root.right, p, q)
            if res: return res

        self.prevElts.pop()
        return None
