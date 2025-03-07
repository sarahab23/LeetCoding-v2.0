class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # stack of time
        posSpd = []
        res = 0

        for i in range(len(position)):
            posSpd.append([position[i], speed[i]])
        
        posSpd.sort(key=lambda x: x[0], reverse=True)

        for i in range(len(position)):
            time = (target - posSpd[i][0])/posSpd[i][1]
            if not stack: stack.append(time)
            else:
                while stack and stack[-1] < time:
                    stack.pop()
                if not stack: res += 1
                stack.append(time)
        
        return res + 1 if stack else res