import sys
class Solution:
    maxsum=-sys.maxsize
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getMax(node):
            if not node:return 0
            l=getMax(node.left);r=getMax(node.right)
            lsum=l+node.val;rsum=r+node.val;asum=l+r+node.val;osum=node.val
            msum=max(osum,max(lsum,rsum))
            self.maxsum=max(self.maxsum,max(asum,msum))
            return msum
        getMax(root)
        return self.maxsum
