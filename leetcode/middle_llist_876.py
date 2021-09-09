class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list=[]
        count=0
        while head:
            count+=1
            list.append(head)
            head=head.next
       # print()
        return list[count//2]