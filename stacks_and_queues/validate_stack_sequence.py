def validate(pushed, popped):
	stack = []
	idx1 = 0
	idx2 = 0
	n = len(pushed)

	while idx1<n or idx2<n:
		if stack and stack[-1] == popped[idx2]:
			stack.pop()
			idx2+=1

		elif idx1<n:
			stack.append(pushed[idx1])
			idx1+=1

		else:
			return False
	return True


pushed = [1,2,3,4,5]
popped = [4,5,3,1,2]
print(validate(pushed, popped))