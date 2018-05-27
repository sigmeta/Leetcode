class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def func(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node
            elif not node.left:
                return func(node.right)
            elif not node.right:
                left_last=func(node.left)
                node.right=node.left
                node.left=None
                return left_last
            else:
                left_last=func(node.left)
                right_last=func(node.right)
                left_last.right=node.right
                node.right=node.left
                node.left=None
                return right_last
        func(root)
