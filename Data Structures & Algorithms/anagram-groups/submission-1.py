class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # dict1=defaultdict(list)
        # for i in strs:
        #     i1="".join(sorted(i))
        #     dict1[i1].append(i)
        # return list(dict1.values())
        
        dict1=defaultdict(list)
        for i in strs:
            count1=[0]*26
            for c in i:
                count1[ord(c)-ord('a')]+=1
            dict1[tuple(count1)].append(i)
        return list(dict1.values())