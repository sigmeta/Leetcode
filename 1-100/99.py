# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.s1,self.s2,self.pre=None,None,None
        def traverse(node):
            if not node: 
                return
            traverse(node.left)
            if self.pre and self.pre.val>node.val:
                if not self.s1:
                    self.s1=self.pre
                self.s2=node
            self.pre=node
            traverse(node.right)
        traverse(root)
        self.s1.val,self.s2.val=self.s2.val,self.s1.val
