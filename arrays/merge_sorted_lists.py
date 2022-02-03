# PROBLEM STATEMENT - Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.

# INPUT - list1 = [1,3,4,5], list2 = [2,6,7,8]


'''
Idea 1(EXTRA SPACE)
- Create a new empty list
- define three variables initialized to 0, to denote current lengths of all three arrays
- Traverse through both the lists simultaneously while comparing the elements
- The min of the two elements will be appended to new list
- If one of the list runs out of elements, just add the remaining of second list to new list
'''

def merge_list(arr1, arr2):
	result = []

	idxArr1 = 0
	idxArr2 = 0
	idxRes = 0

	for i in range(len(arr1) + len(arr2)):
		result.append(i)

	print(result)

	while (idxArr1 < len(arr1)) and (idxArr2 < len(arr2)):
		if arr1[idxArr1] < arr2[idxArr2]:
			result[idxRes] = arr1[idxArr1]
			idxRes += 1
			idxArr1 += 1

		else:
			result[idxRes] = arr2[idxArr2]
			idxRes += 1
			idxArr2 += 1

	while idxArr1 < len(arr1):
		result[idxRes] = arr1[idxArr1]
		idxRes += 1
		idxArr1 += 1

	while idxArr2 < len(arr2):
		result[idxRes] = arr2[idxArr2]
		idxRes += 1
		idxArr2 += 1

	return result

print(merge_list([4, 5, 6], [-2, -1, 0, 7]))