class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        list1=[]
        for i in range(n-2):
        
            if  i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            left=i+1
            right=n-1
            while left<right:
                sum=nums[left]+nums[right]
                if sum==target:
                    list1.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif sum<target:
                    left+=1
                else:
                    right-=1
        return list1

                



