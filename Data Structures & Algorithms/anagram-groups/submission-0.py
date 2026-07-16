class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1=defaultdict(list)
        for i in strs:
            i1="".join(sorted(i))
            dict1[i1].append(i)
        return list(dict1.values())
        
