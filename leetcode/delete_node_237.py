class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp=node.next #go next node
        node.val=temp.val #update current node val
        node.next=temp.next
        temp=None # free up next node