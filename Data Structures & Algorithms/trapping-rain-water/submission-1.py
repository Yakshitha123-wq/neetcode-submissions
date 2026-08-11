class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        lmax=height[left]
        rmax=height[right]
        area=0
        while left<right:
            if lmax<rmax:
                left+=1
                lmax=max(lmax,height[left])
                area+=lmax-height[left]
            else:
                right-=1
                rmax=max(rmax,height[right])
                area+=rmax-height[right]
        return area