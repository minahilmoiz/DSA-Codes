# **********************OBJECT 01**************************************************
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}
        self.adj_matrix = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        u_index = self.vertices.index(u)
        v_index = self.vertices.index(v)
        self.adj_matrix[u_index][v_index] = 1
        self.adj_matrix[v_index][u_index] = 1

    def print_adj_list(self):
        print("Adjacency List:")
        for vertex in self.adj_list:
            print(vertex, "->", " -> ".join(str(adj_vertex) for adj_vertex in self.adj_list[vertex]))

    def print_adj_matrix(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(str(col) for col in row))

# Create a graph with 5 string vertices
vertices = ["A", "B", "C", "D", "E", "F"]
g = Graph(vertices)

# Add edges to the graph
g.add_edge('A', 'B')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'C')
g.add_edge('C', 'E')
g.add_edge('C', 'F')
g.add_edge('D','E')
g.add_edge('D','F')

# Print the adjacency list and matrix of the graph
g.print_adj_list()
g.print_adj_matrix()

#********************************* OBJECT 2 ****************************************

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited

# define the graph as a dictionary with vertex keys and list values
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# call the dfs function with the starting vertex 'A'
visited_vertices = dfs(graph, 'A')

# print the visited vertices
print(visited_vertices)

#-------------------------------------------------

# BFS algorithm in Python
import collections
# BFS algorithm
def bfs(graph, root):

    visited = set()
    queue = collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
print("Following is Breadth First Traversal: ")
bfs(graph, 0)

