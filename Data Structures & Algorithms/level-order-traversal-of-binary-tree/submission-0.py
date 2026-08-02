from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes=[]
        q=deque([root])
        while q:
            list1=[]
           
            qlen=len(q)
            for _ in range(qlen):
                curr=q.popleft()
                list1.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            nodes.append(list1)
        return nodes
        