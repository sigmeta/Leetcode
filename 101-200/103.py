# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        res=[]
        valsnow=[];nodesnow=[];nodesbefore=[root]
        tag=False
        while nodesbefore!=[]:
            if tag:
                res.append([node.val for node in nodesbefore[::-1]])
            else:
                res.append([node.val for node in nodesbefore])
            tag=not tag
            for node in nodesbefore:
                if node.left: nodesnow.append(node.left)
                if node.right: nodesnow.append(node.right)
            nodesbefore=nodesnow
            nodesnow=[]
        return res
