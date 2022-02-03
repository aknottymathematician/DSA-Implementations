'''
Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.
'''

def brute_force(arr):
	product = []
	left = 1
	for i in range(len(arr)):
		currProd = 1
		for j in arr[i+1:]:
			currProd = currProd * j

		product.append(currProd*left)
		left = left * arr[i]

	return product


def optimized(arr):
	product = []
	left = 1
	for i in arr:
		product.append(left)
		left = left * arr[i]

	right = 1
	for i in range(len(arr)-1, -1, -1):
		product[i] = product[i] * right
		right = right * arr[i]
	return product

print(optimized([1, 2, 3, 4]))

