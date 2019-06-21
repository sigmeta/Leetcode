# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s1=[]
        s2=[]
        r=root
        while True:
            s1.append(r)
            if r.val==p.val:
                break
            elif p.val<r.val:
                r=r.left
            else:
                r=r.right
        r=root
        while True:
            s2.append(r)
            if r.val==q.val:
                break
            elif q.val<r.val:
                r=r.left
            else:
                r=r.right
        length=min(len(s1),len(s2))
        s1=s1[:length]
        s2=s2[:length]
        while s1:
            v1=s1.pop();v2=s2.pop()
            if v1.val==v2.val:
                return v1
