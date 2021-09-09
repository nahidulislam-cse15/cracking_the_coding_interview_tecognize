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


#reverse linkid list  recursive way
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #rucursive
       # print(head.val)
#         #newhead=None
#         if head is None:
#             return head
#         if head.next is None:
#             self.head=head
#            # print(newhead.val)
#             return head
        
#         self.reverseList(head.next)
#         #print(head.val)
#         prev=head.next
#         #print(prev.val)
#         prev.next=head
#         #print(prev.next.val)
#         head.next=None
#         return self.head
        if not head or not head.next :
            return head
        reverse=self.reverseList(head.next)
        print(reverse)
        print(reverse.val)
        head.next.next=head
        print("linking head" ,head.next.val)
        print(" head" ,head.val)
        head.next=None   
        return reverse

    
            