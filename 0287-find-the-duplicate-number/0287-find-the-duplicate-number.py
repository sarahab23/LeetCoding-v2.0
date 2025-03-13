class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        meet = fast
        slow = 0
        while True:
            slow = nums[slow]
            meet = nums[meet]
            if slow == meet:
                break
        
        return meet