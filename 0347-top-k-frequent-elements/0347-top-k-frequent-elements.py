class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        prevNums = defaultdict(int) # gives all keys(exist/non exist) values 0 

        for n in nums:
            prevNums[n] += 1
        
        sortedPrevN = sorted(prevNums.items(), key = lambda x: x[1], reverse = True)
        # sorting dict values in desc - prevNums.items() - [(),(),()] - list of tuples
        # key = lambda x: x[1] -> says for each items, sort by item[1] - so value

        for i in range(k):
            res.append(sortedPrevN[i][0])

        return res