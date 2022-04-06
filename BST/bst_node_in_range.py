# Problem: Find the no. of nodes in a BST that lies in a given range

# Algorithm: We will traverse the tree recursively until we encounter leaf nodes (Base case)
# else we do the following
# 1. Current node is less than the given range --> Traverse the right subtree
# 2. Current node is more than the given range --> Traverse the left subtree
# 3. Current node lies in the given range      --> Increment Count; Traverse both the left and right subtree

# Data Structure for Tree Node

# from platform import node
# from tkinter.messagebox import NO


class Node:
    def __init__(self, data):
        self.data = data
        self.rightchild = None
        self.leftchild = None
        

def nodes_in_range(root, rang):
    low, high = rang

    if root==None:
        return 0
    elif root.data==high or root.data==low:
        return 1

    elif root.data<=high or root.data>=low:
        return (1 + nodes_in_range(root.leftchild, rang) + nodes_in_range(root.rightchild, rang))
    elif root.data>high:
        return nodes_in_range(root.leftchild, rang)
    elif root.data<low:
        return nodes_in_range(root.rightchild, rang)


if __name__ == '__main__':
    node = Node(5)
    node.leftchild = Node(3)
    node.rightchild = Node(7)
    node.leftchild.leftchild = Node(2)
    node.leftchild.rightchild = Node(4)
    node.rightchild.rightchild = Node(9)
    node.rightchild.leftchild = Node(6)

    result = nodes_in_range(node, (3, 8))
    print(result)
