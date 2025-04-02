class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, total):
            if target == total:
                res.append(curr[:])
                return
            if total > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res