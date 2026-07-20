class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            list1=[]
        
            for i in range(len(temperatures)):
                for j in range(i+1,len(temperatures)):
                    if temperatures[i]<temperatures[j]:
                        list1.append(j-i)
                        break
                else:
                    list1.append(0)
            return list1
            
                
                     
                    
        