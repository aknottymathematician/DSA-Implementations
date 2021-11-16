def quickSort(arr, low, high):
	if low<high:
		partition_pos = partition(arr, low, high)
		quickSort(arr, low, partition_pos-1)
		quickSort(arr, partition_pos+1, high)

def partition(arr, low, high):
	i = low
	j = high - 1
	pivot = arr[high]
	while i < j:
		while arr[i]<pivot and i<high:
			i = i+1
		while arr[j]>= pivot and j>low:
			j = j-1
		if i<j:
			arr[i], arr[j] = arr[j], arr[i]
	if arr[i]>pivot:
		arr[i], arr[high] = arr[high], arr[i]
	return i

array = [ 10, 7, 8, 9, 1, 5 ]
quickSort(array, 0, len(array) - 1)
  
print(f'Sorted array: {array}')