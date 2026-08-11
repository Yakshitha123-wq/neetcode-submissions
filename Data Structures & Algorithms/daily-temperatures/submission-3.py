class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            
            n=len(temperatures)
            res=[0]*n
            stack=[]
            for i,currtemp in enumerate(temperatures):
                while stack and currtemp>temperatures[stack[-1]]:
                    prevIndex=stack.pop()
                    res[prevIndex]=i-prevIndex
                stack.append(i)
            return res
            
        