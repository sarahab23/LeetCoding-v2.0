class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res,length = [], len(nums)
        bucket = [[] for i in range(length + 1)]
        numCount = defaultdict(int)

        for n in nums:
            numCount[n] += 1 # numCount[n] = numCount.get(n,0) + 1

        for key,val in numCount.items():
            bucket[val] += [key]
        
        for i in range(length, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res

        return