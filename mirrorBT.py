class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isMirror(node1,node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    return (node1.data == node2.data and isMirror(node1.left,node2.right) and isMirror(node1.right,node2.left))
        
    
root1 = Node(1)
root2 = Node(1)
 
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(5)
root2.right.right = Node(4)

if isMirror(root1,root2):
    print("Mirror")
else:
    print("Non Mirror")
