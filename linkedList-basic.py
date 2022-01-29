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
     
    #Get middle element
    def middle(self):
        ptr1 = self.head
        ptr2 = self.head

        while ptr2 and ptr2.next:
            ptr2 = ptr2.next.next
            ptr1 = ptr1.next

        return ptr1.val
    
    #Delete Duplicate element
    def delDup(self):
        ptr1 = self.head
        ptr2 = self.head.next
        
        while ptr2.next:
            if ptr1.val == ptr2.val:
                temp = ptr2.next
                ptr2.next = None
                ptr2 = temp
            else:
                ptr1 = ptr2
                ptr2 = ptr2.next
            print(ptr1.val,ptr2.val)
    
    #Delete middle element
    def delMiddle(self):
        prev = None
        ptr1 = self.head
        ptr2 = self.head
        
        while ptr2 and ptr2.next:
            ptr2 = ptr2.next.next
            prev = ptr1
            ptr1 = ptr1.next
        
        prev.next = ptr1.next
        ptr1.next = None
    
    #Reverse Linked List
    def reverse(self):
        prev = None
        curr = self.head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
    
    #Converting and joining the value and create a string
    def convertStr(self):
        ptr = self.head
        lst = []
        while ptr:
            lst.append(str(ptr.val))
            ptr = ptr.next
        return "".join(lst)
    
    #Check palindrome linked list
    def isPalindrome(self):
        str1 = self.convertStr()
        self.reverse()
        str2 = self.convertStr()
        if str1 == str2:
            print("Palindrome")
        else:
            print("Not palindrome")

llist = linkedList()
temp = ['a','a','b','a','a','c','a']
for i in temp:
        llist.push(i)
llist.printList()
llist.isPalindrome()
