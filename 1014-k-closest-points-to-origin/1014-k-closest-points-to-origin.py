class Solution:
    # TC = O(NlogN) | SC = O(N + k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res, distances = [], []
        for i in range(len(points)):
            d = math.sqrt(pow(points[i][0],2) + pow(points[i][1],2)) # math.sqrt not required. We only take integers. If -1 < no. < 1, then sqrt(no.) > no.
            distances.append([i, d])
        
        distances.sort(key= lambda x: x[1])

        for i in range(k): res.append(points[distances[i][0]])
        return res
