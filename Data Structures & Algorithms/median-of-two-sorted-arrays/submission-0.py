class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m1=nums1+nums2
        m1.sort()
        n=len(m1)
        if n%2==0:
            return (m1[n//2-1]+m1[n//2])/2.0
        else:
            return m1[n//2]
        