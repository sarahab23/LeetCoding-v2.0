class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        prevTime = 0
        pairs = zip(position, speed)

        for p,s in sorted(pairs, reverse = True):
            time = (target - p)/s
            if time > prevTime: 
                res += 1
                prevTime = time
        
        return res