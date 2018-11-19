# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        h1=h2=head;
        while h2.next and h2.next.next:
            h1=h1.next
            h2=h2.next.next
        hm=h1.next
        h1.next=None
        head=self.sortList(head)
        hm=self.sortList(hm)
        if head.val>hm.val:
            head,hm=hm,head
        res=head
        while head.next and hm:
            if hm.val<head.next.val:
                tmp=hm
                hm=hm.next
                tmp.next=head.next
                head.next=tmp
            head=head.next
        if not head.next:
            head.next=hm
        return res
