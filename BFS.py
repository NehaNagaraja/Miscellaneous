class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def BFS(root):
    if root:
        queue = []
        queue.append(root)

        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)