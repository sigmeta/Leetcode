# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        h=ListNode(0)
        h.next=node
        while h.next.next:
            h.next.val=h.next.next.val
            h=h.next
        h.next=None
        return
        
