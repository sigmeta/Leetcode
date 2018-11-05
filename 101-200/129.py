# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue=[[root,root.val]]
        rlist=[]
        i=0
        while i<len(queue):
            node,v=queue[i]
            if node.left:
                queue.append([node.left,v*10+node.left.val])
            if node.right:
                queue.append([node.right,v*10+node.right.val])
            if not node.left and not node.right:
                rlist.append(v)
            i+=1
        return sum(rlist)
