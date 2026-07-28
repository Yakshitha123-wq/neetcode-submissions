class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        res=0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[r])
            res=max(res,r-left+1)
        return res
        