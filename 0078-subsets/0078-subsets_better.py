class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def getAns(nums, i, s):
            if i == len(nums): 
                res.append(s[:])
                return
            getAns(nums, i + 1, s)
            s.append(nums[i])
            getAns(nums, i + 1, s)
            s.pop()
        
        getAns(nums, 0, [])
        return res
