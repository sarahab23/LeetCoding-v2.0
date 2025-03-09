class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l)// 2
            if nums[l] < nums[r]: r = mid - 1
            else:
                if nums[mid] > nums[r]: l = mid + 1
                else: 
                    if nums[mid - 1] > nums[mid]: l = mid
                    else: r = mid - 1
        
        return nums[l]