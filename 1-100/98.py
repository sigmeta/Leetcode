# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:   #判断中序遍历的节点序列是否递增
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        inlist=[]
        self.inorder(root,inlist)
        for i in range(1,len(inlist)):
            if inlist[i]<=inlist[i-1]:
                return False
        return True
    def inorder(self,node,inlist):
        if node.left:
            self.inorder(node.left,inlist)
        inlist.append(node.val)
        if node.right:
            self.inorder(node.right,inlist)
        return
