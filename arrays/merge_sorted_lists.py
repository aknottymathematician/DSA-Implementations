# PROBLEM STATEMENT - Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.

# INPUT - list1 = [1,3,4,5], list2 = [2,6,7,8]


'''
Idea 1(EXTRA SPACE)
Time and Space Complexity O(m+n)
- Create a new empty list
- define three variables initialized to 0, to denote current lengths of all three arrays
- Traverse through both the lists simultaneously while comparing the elements
- The min of the two elements will be appended to new list
- If one of the list runs out of elements, just add the remaining of second list to new list
'''

def merge_list1(arr1, arr2):
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


'''
Idea 1(NO EXTRA SPACE)
Time is O(m(m+n)) and Space Complexity O(1) since we did not use any extra space
- Create two new variables to keep track of current index of both variables
- Compare two lists 
- If elements of list1 is greater than elements of list2 insert list2 element and increment both index numbers
- Else just shift index of lest1 to right
- If len of list1 is smaller than list2, simply add remaining elements to list1 using extend function
'''

def merge_list2(arr1, arr2):
	idx1 = 0
	idx2 = 0

	while idx1 < len(arr1) and idx2 < len(arr2):
		if arr1[idx1] > arr2[idx2]:
			arr1.insert(idx1, arr2[idx2])
			idx1 += 1
			idx2 += 1
		else:
			idx1 += 1

	if idx2 < len(arr2):
		arr1.extend(arr2[idx2:])

	return arr1

print(merge_list2([4, 5, 6], [-2, -1, 0, 7]))

