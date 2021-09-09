class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev=head
        run=head.next
        while run:
            if(prev.val!=run.val):
                prev.next=run
                prev=prev.next
            run=run.next
        prev.next=None
        return head