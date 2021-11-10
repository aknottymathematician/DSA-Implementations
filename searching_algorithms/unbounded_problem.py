"""
Unbounded Binary Search Example (Find the point where a 
monotonically increasing function becomes positive first time)
"""


def f(x):
	return x*x-10*x-20

def firstPositive():
	if f(0)>0:
		return 0

	i = 1
	while f(i)<=0:
		i = i*2
	return binarySearch(i/2,i)

def binarySearch(l, r):
	if r>=l:
		mid = l+(r-l)//2
		if f(mid)>0 and (mid==l or f(mid-1)<=0):
			return mid
		if f(mid)<=0:
			return binarySearch(mid+1, r)
		else:
			return binarySearch(l, mid-1)
	return -1

print(firstPositive())