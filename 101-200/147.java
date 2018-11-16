/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        if(head==null || head.next==null)
            return head;
        ListNode t=head;
        ListNode h=new ListNode(-1);
        h.next=head;
        head=h;
        while(t.next!=null) {
            h=head;
            while(h!=t) {
                if(t.next.val<h.next.val){
                    ListNode tmp=t.next;
                    t.next=tmp.next;
                    tmp.next=h.next;
                    h.next=tmp;
                    break;
                }
                h=h.next;
            }
            if(h==t) {
                t=t.next;
            }
        }
        return head.next;
    }
}
