# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        res=[]
        valsnow=[];nodesnow=[];nodesbefore=[root]
        while nodesbefore!=[]:
            res.append([node.val for node in nodesbefore])
            for node in nodesbefore:
                if node.left: nodesnow.append(node.left)
                if node.right: nodesnow.append(node.right)
            nodesbefore=nodesnow
            nodesnow=[]
        return res
