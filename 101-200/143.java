/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        //find middle
        if(head==null || head.next==null || head.next.next==null){
            return ;
        }
        ListNode h1=head;
        ListNode h2=head.next;
        while(h2.next!=null && h2.next.next!=null){
            h2=h2.next.next;
            h1=h1.next;
        }
        ListNode mid=h1;
        
        //reverse
        h1=mid.next;
        if(h1!=null && h1.next!=null){
            h2=h1.next;
            h1.next=null;
            ListNode h3=h2.next;
            while(h2!=null){
                h3=h2.next;
                h2.next=h1;
                h1=h2;
                h2=h3;
            }
            mid.next=h1;
        }
        h1=mid.next;
        mid.next=null;
        mid=h1;
        //merge
        h1=head;ListNode h3=mid;
        while(h1!=null && mid!=null){
            h2=h1.next;
            h3=mid.next;
            h1.next=mid;
            if(h2!=null){
                mid.next=h2;
            }
            
            h1=h2;
            mid=h3;
            
        }
        
    }
}
