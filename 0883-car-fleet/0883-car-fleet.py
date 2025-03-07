class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = [] # stack of time
        posSpd = [] # pairs of [pos, speed]
        res = 0

        for i in range(n):
            posSpd.append([position[i], speed[i]])
        
        posSpd.sort(key=lambda x: x[0], reverse=True) # Sort in descending order of position

        for i in range(n):
            time = (target - posSpd[i][0])/posSpd[i][1]
            if not stack: stack.append(time)
            else:
                while stack and stack[-1] < time:
                    stack.pop()
                if not stack: res += 1
                stack.append(time)
        
        return res + 1