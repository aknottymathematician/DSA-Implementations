def simplifyPath(path):
	stack = []
	cur = ""

	#reason for adding adding / in for loop is to take care of edge case where input does not end with /
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

path = "/a//b////c/d//././/.."
print(simplifyPath(path))