class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min=[]
        for i in nums:
            heapq.heappush(min,i)
            if len(min)>k:
                heapq.heappop(min)
        return min[0]