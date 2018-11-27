# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ha=headA;hb=headB
        while ha and hb:
            ha=ha.next;hb=hb.next
        if not ha:
            ha,hb=hb,ha
            headA,headB=headB,headA
        diff=0
        while ha:
            diff+=1
            ha=ha.next
        ha=headA;hb=headB
        while diff>0:
            ha=ha.next
            diff-=1
        while ha:
            if ha==hb:
                return ha
            ha=ha.next;hb=hb.next
        return None
