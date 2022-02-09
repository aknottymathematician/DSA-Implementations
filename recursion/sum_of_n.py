def sumofN(n):
	if n == 1:
		return 1
	else:
		return n + sumofN(n-1)

print(sumofN(100))