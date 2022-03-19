def removeDuplicates(string):
	last_occ = {c:i for i, c in enumerate(string)}
	stack = []
	visited = set()

	for i, symbol in enumerate(string):
		if symbol in visited:
			continue

		while stack and symbol<stack[-1] and last_occ[stack[-1]]>i:
			visited.remove(stack.pop())

		stack.append(symbol)
		visited.add(symbol)

	return "".join(stack)

string = "cbacdcbdc"
print(removeDuplicates(string))