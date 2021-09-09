# linkedlist implementation
# 1.create node ->create linked list
# 2.add data
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
       # print(self.value)


class NodeList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node   # print(temp.value)

    def disp(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
    # def insertlast(self, node):


class LinkedList:
    def __init__(self, head, tail, size):
        self.head = head
        self.tail = tail
        self.size = size

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            self.tail.next = new_node
        self.tail = new_node
        # self.size+=1

    def search(self, data):
        temp = self.head
        while temp:
            if(temp.value == data):
                print("Search successful:element found")
            temp = temp.next

    def delete(self):
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        self.tail = temp
        self.tail.next = None
      #  self.size-=1

    def length(self):
        self.size = 0
        temp = self.head
        while temp:
            self.size += 1
            temp = temp.next
        return self.size

    def disp(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def reverse(self, l1):
        stack = []
        run = l1
        while run:
            stack.append(run)
            run = run.next
        self.head = None
        run = None
        while stack:
            temp = stack.pop()
            if self.head is None:
                self.head = temp
                run = temp
            else:
                run.next = temp
                run = run.next
        run.next = None

    def reverse_recur(self, l1):
        if l1.next is None:
            self.head=l1
            return
        self.reverse_recur(l1.next)
        prev=l1.next
        prev.next = l1
        l1.next=None
     def deleteDuplicates(self, head):
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

            

# a=[1,2,3,4,5]
# list=NodeList()
# # head=None
# # temp=None
# for ele in a:
#      new_node=Node(ele)
#      list.insert(new_node)
# #     if head is None:
# #         head=new_node
# #         temp=new_node
# #     else:
# #         temp.next=new_node
# #         temp=temp.next
# # currentnode=head
# # while currentnode:
# #     print(currentnode.value)
# #     currentnode=currentnode.next
# # print(ccu)
# #node1=Node(1)
# #print(node1.value)
# # node2=Node(2)
# # node3=Node(3)
# # list=NodeList()
# # firstnode=list.insert(node1)
# # secondnode=list.insert(node2)
# # thirdnode=list.insert(node3)
# list.insert(Node(6))
list = LinkedList(None, None, 0)
list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.disp()
list.search(3)
list.delete()
list.disp()
print("size:", list.length())

list.insert(10)
# print("size:", list.length())
# print(list.head.value)
list.disp()
list.reverse(list.head)
list.disp()
list.reverse_recur(list.head)
list.disp()
# print(firstnode)
# print("hello")
