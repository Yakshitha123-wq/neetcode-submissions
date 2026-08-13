class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max=[]
        for x,y in points:
            distance=-(x**2+y**2)
            heapq.heappush(max,[distance,x,y])
            if  len(max)>k:
                heapq.heappop(max)
        res=[]
        while max:
            distance,x,y=heapq.heappop(max)
            res.append([x,y])
        return res
        