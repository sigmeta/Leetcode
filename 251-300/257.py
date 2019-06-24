# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.res=[]
        self.getPath([],root)
        res=[]
        for li in self.res:
            res.append('->'.join(li))
        return res
    def getPath(self,path,root):
        if not root.left and not root.right:
            self.res.append(path+[str(root.val)])
            return
        if root.left:
            self.getPath(path+[str(root.val)],root.left)
        if root.right:
            self.getPath(path+[str(root.val)],root.right)
        return
