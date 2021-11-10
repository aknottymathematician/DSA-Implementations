import math

def jumpSearch(arr, x, n):
	step = math.sqrt(n)
	prev=0
	"""
	Locating the block where the element is present if at all
	"""
	while arr[int(min(step,n))-1]<x:
		prev = step
		step +=math.sqrt(n)
		if prev >=n:
			return -1
	"""
	apply linear search on that block to find the element
	"""
	while arr[int(prev)]<x:
		prev+=1
		if prev>n:
			return -1

	"""
	if the element is found
	"""
	if arr[int(prev)]==x:
		return prev

	return -1


arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
x = 233
n = len(arr)

 
# Print the index where 'x' is located
print("Number" , x, "is at index" ,"%.0f"%jumpSearch(arr, x, n))