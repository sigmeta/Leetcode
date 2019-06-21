# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        len=0
        h=head
        while h:
            len+=1
            h=h.next
        if len<2:
            return True
        halflen=len//2
        h=ListNode(0)
        h.next=head
        p=head;q=head.next
        for i in range(halflen-1):
            p.next=q.next
            q.next=h.next
            h.next=q
            q=p.next
        if len%2==1:
            h2=q.next
        else:
            h2=q
        h1=h.next
        for i in range(halflen):
            if h1.val!=h2.val:
                return False
            else:
                h1=h1.next
                h2=h2.next
        return True
