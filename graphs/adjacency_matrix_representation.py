'''
> Function to add vertice
> Function to add edge
'''

vertices = []
graph = []
vertice_count = 0


def add_vertice(vertice):
	global vertice_count
	if vertice in vertices:
		return "vertice already in Graph"

	vertice_count += 1
	vertices.append(vertice)
	for g in graph:
		g.append(0)
	# temp = []
	# for count in range(vertice_count):
	# 	temp.append(0)
	temp = vertice_count*[0]
	graph.append(temp)

#Directed and Undirected graphs
def add_edge(vertice1, vertice2):
	index1 = vertices.index(vertice1)
	index2 = vertices.index(vertice2)

	#UNDIRECTED GRAPH
	graph[index1][index2] = 1
	graph[index2][index1] = 1

	# #DIRECTED GRAPH v1 -> v2
	# graph[index1, index2] = 1

#Directed and Undirected graphs
def add_edge_cost(vertice1, vertice2, cost):
	index1 = vertices.index(vertice1)
	index2 = vertices.index(vertice2)

	#WEIGHTED UNDIRECTED GRAPH
	graph[index1][index2] = cost
	graph[index2][index1] = cost

	# #WEIGHTED DIRECTED GRAPH v1 -> v2
	# graph[index1, index2] = cost


def print_graph():
	for i in range(vertice_count):
		for j in range(vertice_count):
			print(graph[i][j], end=" ")
		print()

print("Before adding vertices")
print(vertices)
print(graph)

add_vertice("A")
add_vertice("B")
add_vertice("C")
add_vertice("D")

print("After adding vertices")
print_graph()

print("After adding edges")
add_edge("A", "B")
add_edge("B", "D")
add_edge("C", "A")

print_graph()