
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



root = Node("C")

root.left = Node("A")
root.right = Node("M")

root.left.left = Node("A")
root.left.right = Node("R")

root.right.left = Node("A")



def display_tree(node, level=0):
    if node is not None:
        display_tree(node.right, level + 1)
        print("    " * level + node.data)
        display_tree(node.left, level + 1)



def binary_bfs(root):
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)



def binary_dfs(root):
    if root:
        print(root.data, end=" ")
        binary_dfs(root.left)
        binary_dfs(root.right)


print("================================")
print(" ASSESSMENT 3.3 - CAMARA")
print(" NON-LINEAR DATA STRUCTURE")
print("================================")

print("\n1. BINARY TREE")
display_tree(root)

print("\nBFS:", end=" ")
binary_bfs(root)

print("\nDFS (Preorder):", end=" ")
binary_dfs(root)



vertices = ["C", "A", "M", "A", "R", "A"]


graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}



def graph_bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    result = []

    while queue:
        node = queue.popleft()
        result.append(vertices[node])

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result



def graph_dfs(node, visited, result):
    visited.add(node)
    result.append(vertices[node])

    for neighbor in graph[node]:
        if neighbor not in visited:
            graph_dfs(neighbor, visited, result)


print("\n\n2. GRAPH")

print("Vertices:", vertices)

print("\n3. BFS (Breadth-First Search)")
print("Traversal:", " -> ".join(graph_bfs(0)))

print("\n4. DFS (Depth-First Search)")
visited = set()
result = []

graph_dfs(0, visited, result)

print("Traversal:", " -> ".join(result))

print("\n================================")
print("       END OF PROGRAM")
print("================================")
