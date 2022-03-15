def minRemove(string):
	string = list(string)
	stack = []

	for i in range(len(string)):
		if string[i] == "(":
			stack.append(i)

		elif string[i] == ")":
			if stack and string[stack[-1]] == "(":
				stack.pop()
			else:
				stack.append(i)
	while stack:
		del string[stack[-1]]
		stack.pop()

	return "".join(string)


print(minRemove("a)b(c)d"))