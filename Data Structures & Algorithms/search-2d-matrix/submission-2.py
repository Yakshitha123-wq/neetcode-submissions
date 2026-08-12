class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m-1
        row=-1
        while left<=right:
            mid=(left+right)//2
            if target>=matrix[mid][0] and target<=matrix[mid][n-1]:
                row=mid
                break
            elif target>=matrix[mid][0]:
                left=mid+1
            else:
                right=mid-1
        if row==-1:
            return False
        st=0
        end=n-1
       
        while st<=end:
            mid=(st+end)//2
            curr=matrix[row][mid]
            if target==curr:
                return True
            elif target<curr:
                end=mid-1
            else:
                st=mid+1
        return False
        