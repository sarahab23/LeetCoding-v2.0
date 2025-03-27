class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq, maxHeap, q = [0] * 26, [], deque()
        time = 0
        for t in tasks:
            freq[ord(t) - ord('A')] -= 1
        
        for f in freq:
            if f < 0: heapq.heappush(maxHeap, f)
        
        while maxHeap or q:
            if maxHeap:
                now = heapq.heappop(maxHeap)
                now += 1
                if now < 0:
                    q.append([now, time + n])
            while q and q[0][1] == time:
                heapq.heappush(maxHeap, q[0][0])
                q.popleft()
            time += 1
        
        return time
