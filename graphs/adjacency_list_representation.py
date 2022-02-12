'''
> Function to add vertice
> Function to add edge
'''

def add_node(node):
	if node in graph:
		return "Node already present in graph"
	graph[node]=[]

def add_edge(node1, node2):
	if not node1 or not node2 in graph:
		return "Nodes not in graph"
	# Undirected graph
	graph[node1].append(node2)
	graph[node2].append(node1)

	# Directed graph node -> node2
	graph[node1].append(node2)

def add_edge(node1, node2, cost):
	if not node1 or not node2 in graph:
		return "Nodes not in graph"
	# Weighted Undirected graph
	w1 = [node2, cost]
	w2 = [node1, cost]
	graph[node1].append(w1)
	graph[node2].append(w2)

	# Weighted Directed graph node -> node2
	w1 = [node2, cost]
	graph[node1].append(w1)



graph = {}
add_node("A")
print(graph)