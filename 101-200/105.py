# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        order={v:i for i,v in enumerate(inorder)}
        def build(l,r,preorder,order):
            if l>=r:return
            node=TreeNode(preorder[l])
            for i in range(l+1,r):
                if order[preorder[i]]>order[preorder[l]]:
                    node.right=build(i,r,preorder,order)
                    r=i
                    break
            node.left=build(l+1,r,preorder,order)
            return node
        return build(0,len(preorder),preorder,order)
