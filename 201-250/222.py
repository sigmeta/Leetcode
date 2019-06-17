# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        hleft=self.countLevel(root.left)
        hright=self.countLevel(root.right)
        if hleft==hright:
            return 2**hleft+self.countNodes(root.right)
        else:
            return self.countNodes(root.left)+2**hright
        
    def countLevel(self, node):
        if not node:
            return 0
        return 1+max(self.countLevel(node.left),self.countLevel(node.right))
                
                
                
