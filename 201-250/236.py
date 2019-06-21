# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.s=[]
        self.cp=self.cq=False
        self.p=p
        self.q=q
        self.traverse(root)
        length=min(len(self.s1),len(self.s2))
        s1=self.s1[:length]
        s2=self.s2[:length]
        while s1:
            v1=s1.pop();v2=s2.pop()
            if v1.val==v2.val:
                return v1
    def traverse(self,r):
        if self.cp and self.cq:
            return
        self.s.append(r)
        if r.val==self.p.val:
            self.s1=self.s.copy()
            self.cp=True
        elif r.val==self.q.val:
            self.s2=self.s.copy()
            self.cq=True
        if r.left:
            self.traverse(r.left)
        if r.right:
            self.traverse(r.right)
        self.s.pop()
        
