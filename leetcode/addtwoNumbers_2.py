# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1=l1
        h2=l2
        s=c=0
        newhead=runner=None
        while h1 and h2:
            s=h1.val+h2.val+c
            c=s//10
            s=s%10
            temp=ListNode(s)
            if not newhead:
                newhead=temp
                runner=temp
            else:
                runner.next=temp
                runner=runner.next
            h1=h1.next
            h2=h2.next
        if h1:
            while h1:
                s=h1.val+c
                c=s//10
                s=s%10
                runner.next=ListNode(s)
                runner=runner.next
                h1=h1.next
        if h2:
            while h2:
                s=h2.val+c
                c=s//10
                s=s%10
                runner.next=ListNode(s)
                runner=runner.next
                h2=h2.next
        if c:
            runner.next=ListNode(c)
        return newhead