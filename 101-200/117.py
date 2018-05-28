class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        now=root
        head=tail=None
        while now:
            if now.left:
                if not head:head=now.left;tail=head
                else:tail.next=now.left;tail=tail.next
            if now.right:
                if not head:head=now.right;tail=head
                else:tail.next=now.right;tail=tail.next
            if now.next:
                now=now.next
            else:
                if tail:tail.next=None
                now=head
                head=tail=None
