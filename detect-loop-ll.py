class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None
    
    #Push Value in Linked List
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    
    #Print Linked List
    def printList(self):
        node = self.head
        while node:
            print(str(node.val)+"   -->  ",end="")
            node = node.next
        print("NULL")
    
    def isLoop(self):
        s = set()
        ptr = self.head
        while ptr:
            if ptr in s:
                return True
            s.add(ptr)
            ptr = ptr.next
        return False

llist = linkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

if llist.isLoop():
    print("Loop Found")
else:
    print("No loop Found")
