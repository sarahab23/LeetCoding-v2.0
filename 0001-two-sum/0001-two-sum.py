class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        storeNums = {}

        for i in range(len(nums)):
            pairNum = target - nums[i]
            if pairNum in storeNums:
                ans = [i, storeNums[pairNum]]
                return ans
            else:
                storeNums[nums[i]] = i