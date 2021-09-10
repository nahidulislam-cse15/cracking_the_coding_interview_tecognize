class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list=[]
        while head:
            list.append(head.val)
            head=head.next
        start=0
        end=len(list)-1
        while start<end:
            if list[start]!=list[end]:
                return False
            start+=1
            end-=1
        return True