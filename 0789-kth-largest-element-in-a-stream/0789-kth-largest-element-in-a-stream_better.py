import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Worst case would be using Array D.S, sorting array in constructor (TC = O(NlogN)) & in add() you'd do Binary Search + Add new elt - worst case the new 
        # elt goes in the middle, so you have to shift n/2 elts, TC = O(N)
        # Current method, we're using heap. [Adding N elts + Popping N - k elts] Constructor TC = O(NlogN) + O(N - k)(logN)
        # Add() - TC = O(logN)
        self.k = k
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.minHeap = nums

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k: heapq.heappush(self.minHeap, val)
        elif len(self.minHeap) == self.k and val > self.minHeap[0]:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
