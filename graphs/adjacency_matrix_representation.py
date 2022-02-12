'''
> Function to add node
> Function to add edge
'''

nodes = []
graph = []
node_count = 0


def add_node(node):
	global node_count
	if node in nodes:
		return "Node already in Graph"

	node_count += 1
	nodes.append(node)
	for g in graph:
		g.append(0)
	# temp = []
	# for count in range(node_count):
	# 	temp.append(0)
	temp = node_count*[0]
	graph.append(temp)

#Directed and Undirected graphs
def add_edge(node1, node2):
	index1 = nodes.index(node1)
	index2 = nodes.index(node2)

	#UNDIRECTED GRAPH
	graph[index1][index2] = 1
	graph[index2][index1] = 1

	# #DIRECTED GRAPH v1 -> v2
	# graph[index1, index2] = 1



def print_graph():
	for i in range(node_count):
		for j in range(node_count):
			print(graph[i][j], end=" ")
		print()

print("Before adding nodes")
print(nodes)
print(graph)

add_node("A")
add_node("B")
add_node("C")
add_node("D")

print("After adding nodes")
print_graph()

print("After adding edges")
add_edge("A", "B")
add_edge("B", "D")
add_edge("C", "A")

print_graph()