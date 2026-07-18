class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left=0
        right=n-1
        list1=[]
        while left<right:
            sum=numbers[left]+numbers[right]
            if sum==target:
                list1.extend([left+1,right+1])
                
                while left<right and numbers[left]==numbers[left+1]:
                    left+=1
                
                while left<right and numbers[right]==numbers[right-1]:
                    right-=1
                left+=1
                right-=1
            elif sum<target:
                left+=1
            else:
                right-=1
        return list1
        