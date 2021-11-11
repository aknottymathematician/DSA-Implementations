def bubbleSort(arr):
	n = len(arr)
	"""
	Traverse through the whole list
	"""
	for i in range(n):
		"""
		This provision is specially if the array is already sorted, 
		thus giving us the best case scenario 
		"""
		swapped = False
		"""
		Traverse from 0 to n-i-1 since elements post i are already sorted 
		and then swap if incorrectly placed
		"""
		for j in range(0, n-i-1):
			if arr[j]>arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		"""
		Break the loop in case the input list is already sorted
		"""
		if swapped == False:
			break



arr = [64, 34, 25, 12, 22, 11, 90]

# arr = [11, 22, 44, 67, 78, 109]

bubbleSort(arr)
  
print ("Sorted array :")
for i in range(len(arr)):
    print ("%d" %arr[i],end=" ")