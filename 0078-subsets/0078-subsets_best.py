class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums): 
                res.append(subset[:])
                return
            
            # including elt
            subset.append(nums[i])
            dfs(i + 1)

            # without current elt
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
