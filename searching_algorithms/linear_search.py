def linearSearch(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return i
	return -1


arr=[19,23,4,14,6,2,7,8,10,33]
print(linearSearch(arr, 3))