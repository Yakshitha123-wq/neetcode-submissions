from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count=Counter(hand)
        hand.sort()
        for i in hand:
            while count[i]:
                for num in range(i,i+groupSize):
                    if count[num]==0:
                        return False
                    count[num]-=1
        return True
        

        