class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return nums
        nums1=list(set(nums))
        nums1.sort(reverse=True,key=lambda x:nums.count(x))
        return nums1[:k]