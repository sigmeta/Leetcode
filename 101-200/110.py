# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isBal(root):
            if not root:
                return True,0
            lstatus,ldepth=isBal(root.left)
            if not lstatus:return False,-1
            rstatus,rdepth=isBal(root.right)
            if not rstatus:return False,-1
            return abs(ldepth-rdepth)<=1,1+max(ldepth,rdepth)
        return isBal(root)[0]
