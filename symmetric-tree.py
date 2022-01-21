class Node:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
        
def is_symmetric(root1,root2):
    if root1 is None and root2 is None:
        return True
    if ((root is None)!=(root2 is None)) or root1.val != root2.val:
        return False
    else:
        return is_symmetric(root1.left,root2.right) and is_symmetric(root1.right,root2.left)

def symmetric(root):
    if root is None:
        return True
    else:
        return is_symmetric(root.left,root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print(symmetric(root))
