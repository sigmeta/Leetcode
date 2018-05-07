# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def dfs(p,q):
            if not p and not q:
                return True
            elif (p and not q) or (not p and q) or p.val!=q.val:
                return False
            else:
                return dfs(p.left,q.left) and dfs(p.right,q.right)
        return dfs(p,q)
