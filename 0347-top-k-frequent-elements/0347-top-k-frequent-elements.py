class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        prevNums = defaultdict(int)

        for n in nums:
            prevNums[n] += 1
        
        sortedPrevN = sorted(prevNums.items(), key = lambda x: x[1], reverse = True)

        for i in range(k):
            res.append(sortedPrevN[i][0])

        return res