class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res, minHeap = [], []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)

        for i in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        
        return res
