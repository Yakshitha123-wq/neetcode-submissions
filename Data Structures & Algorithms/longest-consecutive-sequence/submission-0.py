class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n1=set(nums)
        longest=0
        
        for i in n1:
            if i-1 not in n1:
                length=1
                while (i+length) in n1:
                    length+=1
                longest=max(longest,length)
        return longest

        