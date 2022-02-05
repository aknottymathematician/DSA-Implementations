'''
Implement a function rearrange(lst) which rearranges the elements such that all 
the negative elements appear on the left and positive elements appear at the right of the list.
Note that it is not necessary to maintain the sorted order of the input list.
'''

# IDEA 1
# AUXILLARY LIST
def brute(arr):
	pos = []
	neg = []

	for i in arr:
		if i >= 0:
			pos.append(i)
		else:
			neg.append(i)
	return neg+pos


# IDEA 2
# IN-PLACE REARRANGEMENT
def inPLace(arr):
	leftMostdigit = 0

	for i in range(len(arr)):
		if arr[i] < 0:
			if i != leftMostdigit:
				#swap
				arr[i], arr[leftMostdigit] = arr[leftMostdigit], arr[i]
			leftMostdigit += 1

	return arr


print(inPLace([10,-1,20,4,5,-9,-6]))

# def foo(value, lst):
#     value = 1
#     print(value)
#     lst[0] = 44

# v = 3
lst = [[1, 2, 3],[1, 2, 3],[1, 2, 3]]
# print(foo(v, lst))
# print(v, lst[0])
print(lst[0].pop())

# def f(i, values = []):
#     values.append(i)
#     print (values),
#     return values
# f(1)
# f(2)
# f(3)