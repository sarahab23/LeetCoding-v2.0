class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       res = float('inf') # min not needed
       maxK = 0
       for n in piles: maxK = max(maxK, n)

       low, high = 1, maxK

       while low <= high:
            hTaken = 0
            k = low + (high - low)//2

            for n in piles:
                hTaken += math.ceil(n/k)
        
            if hTaken > h: low = k + 1
            else:
                res = min(res, k)
                high = k - 1

       return res
       