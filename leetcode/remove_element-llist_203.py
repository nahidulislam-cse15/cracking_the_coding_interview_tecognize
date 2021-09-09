class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        prev=head
        run=head.next
        while run:
            if(run.val!=val):
                prev.next=run
                prev=prev.next
            #prev.next=run
            run=run.next
        prev.next=None
        if head.val==val:
            head=head.next
        return head