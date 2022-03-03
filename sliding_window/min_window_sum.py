def min_window_sum(s, arr):
	wSum = 0
	wStart = 0
	minLen = float('inf')

	for wEnd in range(len(arr)):
		wSum += arr[wEnd]
		while wSum >= s:
			minLen = min(minLen, wEnd-wStart+1)
			wSum -= arr[wStart]
			wStart += 1
	if minLen == float('inf'):
		return 0
	return minLen



def main():
  print("Maximum sum of a subarray of size K: " + str(min_window_sum(6, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(min_window_sum(8, [2, 3, 4, 1, 5])))

main()