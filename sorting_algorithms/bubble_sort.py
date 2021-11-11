def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		swapped = False
		for j in range(0, n-i-1):
			if arr[j]>arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if swapped == False:
			break



arr = [64, 34, 25, 12, 22, 11, 90]

# arr = [11, 22, 44, 67, 78, 109]

bubbleSort(arr)
  
print ("Sorted array :")
for i in range(len(arr)):
    print ("%d" %arr[i],end=" ")