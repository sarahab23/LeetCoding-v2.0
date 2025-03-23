class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res, distances = [], []
        for i in range(len(points)):
            d = pow(points[i][0],2) + pow(points[i][1],2)
            distances.append([i, d])
        
        distances.sort(key= lambda x: x[1])

        for i in range(k): res.append(points[distances[i][0]])
        return res