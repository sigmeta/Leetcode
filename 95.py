# 95. Unique Binary Search Trees II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:          
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        else:
            return self.dfs(1,n+1)
    def dfs(self,s,e):
        res=[]
        if s==e:
            return None
        for i in range(s,e):
            for l in self.dfs(s,i) or [None]:
                for r in self.dfs(i+1,e) or [None]:
                    node=TreeNode(i)
                    node.left=l
                    node.right=r
                    res.append(node)
        return res
