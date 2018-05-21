# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array=[]
        while head:
            array.append(head.val)
            head=head.next
        def arrayToBST(array,l,r):
            if l>=r:return None
            mid=(l+r)//2
            node=TreeNode(array[mid])
            node.left=arrayToBST(array,l,mid)
            node.right=arrayToBST(array,mid+1,r)
            return node
        return arrayToBST(array,0,len(array))
        
