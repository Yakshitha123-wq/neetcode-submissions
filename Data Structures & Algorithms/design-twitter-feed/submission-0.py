import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time=0
        self.followMap=defaultdict(set)
        self.tweetMap=defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweetMap[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        users= self.followMap[userId]|{userId}
        heap=[]
        for user in users:
            if self.tweetMap[user]:
                idx=len(self.tweetMap[user])-1
                time,tweetId=self.tweetMap[user][idx]
                heapq.heappush(heap,(-time,user,idx,tweetId))
        res=[]
        while heap and len(res)<10:
            negTime,user,idx,tweetId=heapq.heappop(heap)
            res.append(tweetId)
            if idx>0:
                idx-=1
                time,tweetId=self.tweetMap[user][idx]
                heapq.heappush(heap,(-time,user,idx,tweetId))
        return res
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
             self.followMap[followerId].remove(followeeId)

        
