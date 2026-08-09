from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        unique1=list(set(nums))
        unique1.sort(reverse=True,key=lambda x:counts[x])
        return unique1[:k]
       