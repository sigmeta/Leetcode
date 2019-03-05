# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        h=ListNode(0)
        h.next=head
        p=h
        while head:
            if head.val==val:
                p.next=head.next
                head=p.next
            else:
                p=p.next
                head=head.next
        return h.next
