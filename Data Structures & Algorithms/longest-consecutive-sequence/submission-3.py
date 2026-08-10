class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n1=set(nums)
        res=0
        for i in n1:
            if i-1 not in n1:
                
                len1=1
                while (i+len1) in n1:
                
            
                   len1+=1
                res=max(res,len1)

        return res
            
        