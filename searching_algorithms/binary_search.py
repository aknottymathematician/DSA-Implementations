# def binarySearch(arr, l, r, x):
# 	"""
# 	This is a recursive approach of Binary Search
# 	"""

# 	if r>l:
# 		mid = l+(r-l)//2
# 		if arr[mid]==x:
# 			return mid
# 		elif arr[mid]>x:
# 			binarySearch(arr, l, mid-1, x)
# 		elif arr[mid]<x:
# 			binarySearch(arr, mid+1, r, x)
# 	else:
# 		return -1

def binarySearch(arr, l, r, x):
	"""
	This is an iterative approach of the Binary Search
	"""
	while l<r:
		mid = l+(r-l)//2
		if arr[mid]==x:
			return mid
		elif arr[mid]>x:
			r=mid-1
		elif arr[mid]<x:
			l=mid+1
	return -1



arr=[1, 6, 19, 34, 56, 90, 119, 133]
print(binarySearch(arr, 0, len(arr)-1, 119))