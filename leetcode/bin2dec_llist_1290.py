class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimalval=0
        list=[]
        while head:
            list.append(head.val)
            head=head.next
        cnt=0
        while list:
            decimalval+=list.pop()*pow(2,cnt)
            cnt+=1
        return decimalval