# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h1=h2=head
        while h2 and h2.next:
            h1=h1.next
            h2=h2.next.next
            if h1==h2:
                h=head
                while h!=h1:
                    h=h.next
                    h1=h1.next
                return h
        return None
