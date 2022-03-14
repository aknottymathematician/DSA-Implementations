def simplifyPath(path):
	stack = []
	cur = ""

	for p in path+"/":
		if p == "/":
			if cur == "..":
				if stack: stack.pop()
			elif cur != "" and cur != ".": 
				#cur could be empty if there are multiple consecutive ?
				stack.append(cur)
			cur = ""
		else:
			cur += p

	return "/" + "/".join(stack)

path = "/home//foo/"
print(simplifyPath(path))