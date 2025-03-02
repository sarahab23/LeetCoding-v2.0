class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pref = 1
        suf = 1
        res = [1] * length

        for i in range(length):
            res[i] *= pref
            pref *= nums[i]

        for i in range(length - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i]
        
        return res
