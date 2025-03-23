import heapq
class Solution:
    # TC of Heapify = O(N) + O(NlogN) = O(NlogN)
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while maxHeap:
            first = heapq.heappop(maxHeap)
            if not maxHeap: return -1 * first
            second = heapq.heappop(maxHeap)
            if first == second: continue
            else: heapq.heappush(maxHeap, first - second)

        return 0
