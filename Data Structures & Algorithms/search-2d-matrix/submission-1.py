class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        start=0
        end=m-1
        row=-1
        while start<=end:
            mid=(start+end)//2
            if target>=matrix[mid][0] and target<=matrix[mid][n-1]:
                row=mid
                break
            elif target>matrix[mid][n-1]:
                start=mid+1
            else:
                end=mid-1
        if row==-1:
            return False
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            curr=matrix[row][mid]
            if target==curr:
                return True
            elif target>curr:
                left=mid+1
            else:
                right=mid-1
        return False
        