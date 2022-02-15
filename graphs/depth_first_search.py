from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFShelper(self, v, visited):

		visited.add(v)

		for neighbour in self.graph[v]:
			if not neighbour in visited:
				self.DFShelper(neighbour, visited)

	def DFS(self, v):
		visited = set()

		return self.DFShelper(v, visited)


# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
print(g.DFS(2))