class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        maxL, maxR = [0] * length, [0] * length
        res = 0

        for i in range(1,length):
            maxL[i] = max(height[i - 1], maxL[i - 1])
        
        for i in range(length - 2, -1, -1):
            maxR[i] = max(height[i + 1], maxR[i + 1])

        for i in range(0, length):
            val = min(maxL[i], maxR[i]) - height[i]
            res += (val if val >= 0 else 0)

        return res
