class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length, res = len(candidates), []
        subset, summ = [], 0
        def dfs(i):
            if i >= length or i < 0:
                return
            nonlocal summ
            summ += candidates[i]
            subset.append(candidates[i])
            if summ > target:
                summ -= candidates[i]
                subset.pop()
                return
            elif summ == target:
                if sorted(subset) not in res:
                    res.append(sorted(subset))
                summ -= candidates[i]
                subset.pop()
                return
            else:
                for j in range(length, -1, -1):
                    dfs(j)
                summ -= candidates[i]
                subset.pop()
        
        for i in range(length, -1, -1):
            dfs(i)
        
        return res