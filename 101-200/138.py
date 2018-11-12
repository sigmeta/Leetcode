# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        res=RandomListNode(head.label)
        h=head
        r=res
        node_dict={head.label:res}
        while h:
            if h.next:
                if h.next.label in node_dict:
                    r.next=node_dict[h.next.label]
                else:
                    r.next=RandomListNode(h.next.label)
                    node_dict[h.next.label]=r.next
            if h.random:
                if h.random.label in node_dict:
                    r.random=node_dict[h.random.label]
                else:
                    r.random=RandomListNode(h.random.label)
                    node_dict[h.random.label]=r.random
            h=h.next;r=r.next
        return res
