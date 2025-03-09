class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low <= high:
            hours = 0
            k = low + (high - low)//2

            for n in piles:
                hours += math.ceil(n/k)
        
            if hours > h: low = k + 1
            else:
                res = min(res, k) # (OR) min(res,k) not necessary. res = k is also correct
                high = k - 1

        return res
       