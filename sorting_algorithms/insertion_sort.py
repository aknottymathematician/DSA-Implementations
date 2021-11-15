def insertionSort(arr):
	for i in range(1, len(arr)):
		j = i
		while arr[j-1]>arr[j] and j>0:
			arr[j-1], arr[j] = arr[j], arr[j-1]
			j -= 1
	return arr


arr = [12, 11, 11, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])