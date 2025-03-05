class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) - 1
        maxL, maxR, res = 0, 0, 0

        while l <= r:
            if maxL <= maxR: 
                val = maxL - height[l]
                res += (val if val > 0 else 0)
                maxL = max(maxL, height[l])
                l += 1
            else: 
                val = maxR - height[r]
                res += (val if val > 0 else 0)
                maxR = max(maxR, height[r])
                r -= 1
        
        return res