"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=[i.start for i in intervals]
        end=[j.end for j in intervals]
        start.sort()
        end.sort()
        count1=0
        s=0
        e=0
        res=0
        while s<len(intervals):
            if start[s]<end[e]:
                s+=1
                
                count1+=1
                res=max(res,count1)
            else:
                e+=1
                count1-=1
        return res
        

       