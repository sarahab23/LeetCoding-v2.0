class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {} # value: index

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevNums:
                return [i, prevNums[diff]]
            else:
                prevNums[nums[i]] = i

        return # for no reason