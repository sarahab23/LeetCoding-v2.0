class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        prevTime = 0 # storing slow prev car's time
        pairs = zip(position, speed) # pairs are iterators of tuples 

        for p,s in sorted(pairs)[::-1]:
            time = (target - p)/s
            if time > prevTime: 
                res += 1
                prevTime = time
        
        return res