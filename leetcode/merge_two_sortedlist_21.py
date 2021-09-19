# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1=l1
        h2=l2
        newhead=ListNode(0)
        runner=newhead
        while h1 and h2:
            if h1.val<=h2.val:
                runner.next=h1
                runner=runner.next
                h1=h1.next 
                
            else:
                runner.next=h2
                runner=runner.next
                h2=h2.next
        while h1:
                runner.next=h1
                runner=runner.next
                h1=h1.next
               
        while h2:
                runner.next=h2
                runner=runner.next
                h2=h2.next
        return newhead.next