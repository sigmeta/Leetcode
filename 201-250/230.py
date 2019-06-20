# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count=0
        self.k=k
        self.res=0
        self.leftTraverse(root)
        return self.res
    
    def leftTraverse(self, root):
        if root.left:
            self.leftTraverse(root.left)
        self.count+=1
        if self.count==self.k:
            self.res=root.val
            return 
        if root.right:
            self.leftTraverse(root.right)
        return
