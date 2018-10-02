class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def Inorder(root):
    if root:
        Inorder(root.left)
        print (root.data)
        Inorder(root.right)

def Preorder(root):
    if root:
        Preorder(root.left)
        Preorder(root.right)
        print (root.data)

def Postorder(root):
    if root:
        print (root.data)
        Postorder(root.left)
        Postorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Inorder")
Inorder(root)
print ("Preorder")
Preorder(root)
print ("Postorder")
Postorder(root)
