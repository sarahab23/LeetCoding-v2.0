class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap, q = [], deque()
        time = 0

        freq = Counter(tasks) # only counts character +nt, not 0
        maxHeap = [-f for f in freq.values()]
        heapq.heapify(maxHeap)
        
        while maxHeap or q:
            if maxHeap:
                now = 1 + heapq.heappop(maxHeap)
                if now: q.append([now, time + n]) # q[-freq, time it can appear]
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            time += 1
        
        return time