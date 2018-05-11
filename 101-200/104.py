class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_depth(node):
            if not node:
                return 0
            else:
                return 1+max(get_depth(node.left),get_depth(node.right))
        return get_depth(root)
