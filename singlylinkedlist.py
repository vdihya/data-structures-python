# SINGLY LINKED LIST
class node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def insertstart(self,data):
        self.size = self.size + 1
        newnode = node(data)

        if not self.head:
            self.head  = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    #def size(self):
      #  print(self.size," is the size of the linked list")

    def size2(self):
        temp = self.head
        size = 0
        while temp is not None:
            size += 1
            temp = temp.next
        
    def insertend(self,data):
        
        self.size += 1
        newnode = node(data)
        temp = self.head
        
        while temp.next is not None:
            temp = temp.next
       
        temp.next = newnode

    def traversal(self):
        temp = self.head
        while temp is not None:
            print("data: ", temp.data)
            temp = temp.next
    def remove(self,data):
        if self.head is None:
            return

        self.size -= 1
        temp = self.head
        prev = None
    
        while temp.data !=data:
            prev = temp
            temp = temp.next
        if prev is None: # the head node itself has data that needs to be delete hence the head has to be deleted
            self.head = temp.next
        else:
            print(temp.data," deleted")
            prev.next = temp.next #temp contains what has to be deleted
linkedlist = linkedlist()

linkedlist.insertstart(10)
linkedlist.insertstart(20)
linkedlist.insertend(50)
linkedlist.traversal()
linkedlist.remove(50)
linkedlist.traversal()
linkedlist.remove(10)
linkedlist.traversal()
#linkedlist.size()



