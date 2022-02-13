'''
> Function to add vertice
> Function to add edge
> Function to delete vertice
> Function to delete edge
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

# Undirected and Unweighted
def delete_node(node):
	if not node in graph:
		print("Node not in graph")
	graph.pop(node)
	for g in graph:
		temp = graph[g]
		if node in temp:
			graph[g].remove(node)

# Weighted Undirected
def delete_node(node):
	if not node in graph:
		print("Node not in graph")
	graph.pop(node)
	for g in graph:
		temp = graph[g]
		for t in temp:
			if node == t[0]:
				temp.remove(node)
				break

def delete_edge(node1, node2):
	if not node1 in graph or not node2 in graph:
		print("node not present in graph")
	#Undirected
	if node2 in graph[node1]:
		graph[node1].remove(node2)
		graph[node2].remove(node1)
	#Directed
	if node2 in graph[node1]:
		graph[node1].remove(node2)

# Weighted
def delete_edge(node1, node2):
	if not node1 in graph or not node2 in graph:
		print("node not present in graph")
	#Undirected
	w1 = [node2, cost]
	w2 = [node1, cost]
	if node2 in graph[node1]:
		graph[node1].remove(w1)
		graph[node2].remove(w2)
	#Directed
	if node2 in graph[node1]:
		graph[node1].remove(w1)


graph = {}
add_node("A")
print(graph)