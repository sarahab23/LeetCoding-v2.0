class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l, r = 0, 0, 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            res = max(res, profit)
            if profit < 0:
                l = r
            else:
                r += 1
        
        return res