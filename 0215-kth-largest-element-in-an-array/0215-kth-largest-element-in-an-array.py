class Solution:
    # Sorting -> O(NlogN)
    # This -> TC = Heapify + k.pop = O(N) + k.O(logN)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        for i in range(k):
            res = -1 * heapq.heappop(maxHeap)

        return res
