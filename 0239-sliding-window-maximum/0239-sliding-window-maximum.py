class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()

        for i in range(0,k):
            if q: # making sure max no. is placed first, followed by decreasing no.s
                while q and nums[q[-1]] < nums[i]: q.pop()
            q.append(i)

        res.append(nums[q[0]])

        l, r = 1, k
        while r < len(nums):
            if (l - 1) == q[0]: q.popleft() # removing prev l
            while q and nums[q[-1]] < nums[r]: q.pop() # adding r
            q.append(r)
            r += 1
            l += 1
            res.append(nums[q[0]])
        
        return res
            


