import heapq
class KthLargest:
    # Current method, we're using heap. [Adding N elts + Popping N - k elts] Constructor TC = O(NlogN) + O(N - k)(logN)
    # Add() - TC = O(logN)
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.minHeap, self.k = nums, k

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k: heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
