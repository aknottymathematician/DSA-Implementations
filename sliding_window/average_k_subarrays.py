def average_k_subarrays(k, arr):
	wSum = 0
	mSum = 0
	mStart = 0

	for mEnd in range(len(arr)):
		wSum += arr[mEnd]
		if mEnd>=k-1:
			mSum = max(mSum, wSum)
			wSum -= arr[mStart]
			mStart+=1
	return mSum


def main():
  print("Maximum sum of a subarray of size K: " + str(average_k_subarrays(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(average_k_subarrays(2, [2, 3, 4, 1, 5])))

main()