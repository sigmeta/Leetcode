# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def getPath(node,sum):
            if not node:
                return False,[]
            elif not node.left and not node.right and node.val==sum:
                return True,[[sum]]
            else:
                ltag,llist=getPath(node.left,sum-node.val)
                rtag,rlist=getPath(node.right,sum-node.val)
                return ltag or rtag,[[node.val]+nlist for nlist in llist+rlist]
        return getPath(root,sum)[1]
