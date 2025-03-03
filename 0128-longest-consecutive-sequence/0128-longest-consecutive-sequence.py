class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        res = 0

        for num in uniqueNums:
            if num - 1 not in uniqueNums:
                streak = 1
                while num + streak in uniqueNums:
                    streak += 1
                res = max(res, streak)

        return res