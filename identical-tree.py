class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def identical(node1,node2):
    if node1 is None and node2 is None:
        return True
    if (node1.data == node2.data and identical(node1.left,node2.left) and identical(node1.right,node2.right)):
        return True
    else:
        return False
        
        
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

if identical(root1,root2):
    print("Trees are identical")
else:
    print("Trees are not identical")
