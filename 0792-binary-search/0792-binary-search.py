class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = l + ((h - l)// 2) # or (l + h)//2 because if l & h is too high, like close to a 32 bit number, then sum of l + h cannot be calculated, this is for other languages like C++/ java
            if nums[mid] > target: h = mid - 1
            elif nums[mid] < target: l = mid + 1
            else: return mid

        return -1