'''
In Breadth First Search Algorithm, we traverse the graph along the breadth, 
i.e. we only move along the adjacent elements.
'''

import collections

def bfs(graph, root):
	visited = set()
	queue = collections.deque([root])
	while queue:
		print(queue)
		vertex = queue.popleft()
		visited.add(vertex)

		for i in graph[vertex]:
			if i not in visited:
				queue.append(i)
	print(visited)



if __name__ == "__main__":
	graph =  {0: [1, 2], 1: [2,3,0], 2: [3,1,0], 3: [1, 2]}
	bfs(graph, 0)

print("OR", 1|4)