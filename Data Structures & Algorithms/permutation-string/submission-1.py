class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1count={}
        for ch in s1:
            s1count[ch]=s1count.get(ch,0)+1
        windowsize=len(s1)
        s2count={}
        for  i in range(windowsize):
            s2count[s2[i]]=s2count.get(s2[i],0)+1
        if s1count==s2count:
            return True
        for r in range(windowsize,len(s2)):
            right=s2[r]
            s2count[right]=s2count.get(right,0)+1
            left=s2[r-windowsize]
            s2count[left]=s2count[left]-1
            if s2count[left]==0:
                del s2count[left]
            if s1count==s2count:
                return True
        return False