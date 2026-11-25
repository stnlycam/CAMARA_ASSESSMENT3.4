class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def display_tree(node, level=0):
    if node is not None:
        display_tree(node.right, level + 1)
        print("    " * level + node.data)
        display_tree(node.left, level + 1)


def preorder(node):
    if node is None:
        return []
    return [node.data] + preorder(node.left) + preorder(node.right)


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.data]


# Binary Tree using STANLEYCAMARA (First Name + Last Name)
root = Node("S")

root.left = Node("T")
root.right = Node("A")

root.left.left = Node("N")
root.left.right = Node("L")
root.right.left = Node("E")
root.right.right = Node("Y")

root.left.left.left = Node("C")
root.left.left.right = Node("A")
root.left.right.left = Node("M")
root.left.right.right = Node("A")
root.right.left.left = Node("R")
root.right.left.right = Node("A")

print("=========================================")
print(" ASSESSMENT 3.6 - DFS METHODS IN TREE")
print(" NAME: STANLEY CAMARA")
print("=========================================")

print("\nBinary Tree Structure:")
display_tree(root)

print("\nPreorder  (Root -> Left -> Right):")
print(" -> ".join(preorder(root)))

print("\nInorder   (Left -> Root -> Right):")
print(" -> ".join(inorder(root)))

print("\nPostorder (Left -> Right -> Root):")
print(" -> ".join(postorder(root)))

print("\n=========================================")
print("             END OF PROGRAM")
print("=========================================")
