class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pref = [1] * length
        suf = [1] * length
        res = [1] * length

        for i in range(1, length, 1):
            pref[i] = nums[i - 1] * pref[i - 1]

        for i in range(length - 2, -1, -1):
            suf[i] = nums[i + 1] * suf[i + 1]

        for i in range(length):
            res[i] = pref[i] * suf[i]
        
        return res
