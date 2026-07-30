class Solution:
    def minWindow(self, s: str, t: str) -> str:
        scount={}
        tcount={}
       
        res=[-1,-1]
        reslen=float("inf")
        for char in t:
            tcount[char]=tcount.get(char,0)+1
        have=0
        need=len(tcount)
        l=0
        for r in range(len(s)):
            c=s[r]
            scount[c]=scount.get(c,0)+1
            if c in tcount and scount[c]==tcount[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                left=s[l]
                scount[left]-=1
                if left  in tcount and scount[left]<tcount[left]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float("inf") else ""

        