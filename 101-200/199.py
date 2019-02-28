# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        tree=[[root]]
        i=0
        while i<len(tree):
            nl=[]
            for n in tree[i]:
                if n.left:
                    nl.append(n.left)
                if n.right:
                    nl.append(n.right)
            if nl:
                tree.append(nl)
            i+=1
        return [nl[-1].val for nl in tree]
