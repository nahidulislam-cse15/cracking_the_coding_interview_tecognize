# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #iterarivly using stack
        # stack=[]
        # reverselist=[]
        # run=head
        # while run:
        #     stack.append(run)
        #     #print(run.val)
        #     run=run.next
        # newhead=None
        # run=None
        # while stack:
        #     temp=stack.pop()
        #     if newhead is None:
        #         newhead=temp
        #         run=temp  
        #     else:
        #         run.next=temp
        #         #reverselist.append(temp)
        #         run=run.next
        # run.next=None 
        # return newhead
    
    #iterative two pointer
        prev=None
        run=head
        while run:
            temp=run.next #
            run.next=prev
            prev=run
            run=temp
        return prev

    
            