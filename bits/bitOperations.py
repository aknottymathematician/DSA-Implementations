# Count number of digits in n

def countN(n):
	count = 0
	while n>0:
		n = n//10
		count+=1
	return count

print(countN(1234))


#number of bits in binary

def bitsInBinary1(n):
	count = 0
	while n>0:
		count +=1
		n>>=1

	return count

def bitsInBinary2(n):
	stack = []
	while n>0:
		print(stack)
		rem = n%2
		stack.append(rem)
		n = n//2
	print(stack)
	while stack:
		binary = stack.pop()
		print(binary)

print(bitsInBinary1(10))

# AND operator
def andOp(x, y):
	print(x & y)
print((5&1)==1)
# print(andOp(2, 5))