# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head
        h=ListNode(0)
        h.next=head
        p=h
        while head.next:
            q=head.next
            head.next=q.next
            q.next=h.next
            h.next=q
        return h.next
