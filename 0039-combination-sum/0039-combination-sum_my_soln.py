class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length, res, subset, total = len(candidates), [], [], 0
        def dfs(i):
            # if i >= length or i < 0:
            #     return
            nonlocal total
            total += candidates[i]
            subset.append(candidates[i])
            if total > target:
                total -= candidates[i]
                subset.pop()
                return
            elif total == target:
                if sorted(subset) not in res:
                    res.append(sorted(subset))
                total -= candidates[i]
                subset.pop()
                return
            else:
                for j in range(length - 1, -1, -1):
                    dfs(j)
                total -= candidates[i]
                subset.pop()
        
        for i in range(length - 1, -1, -1):
            dfs(i)
        
        return res
