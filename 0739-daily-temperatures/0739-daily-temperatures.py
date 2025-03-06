class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stack of pairs [val, pos]
        res = [0] * len(temperatures)

        for i, n in enumerate(temperatures[::-1]):
            while stack and stack[-1][0] <= n:
                stack.pop()
            if stack: res[i] = i - stack[-1][1]
            stack.append([n,i])

        return res[::-1]