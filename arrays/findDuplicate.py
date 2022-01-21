## METHOD I brute force
# Time Complexity - O(N^2), Space Complexity - O(1)
def findDuplicate(array):
    minsecIndex = len(array)
    for i in range(len(array)):
        value = array[i]
        for j in range(i+1,len(array)):
            valueToCompare = array[j]
            if value == valueToCompare:
                minsecIndex = min(minsecIndex, j)
    if minsecIndex == len(array):
        return -1
    return array[minsecIndex]


## METHOD II using set
# Time Complexity - O(N), Space Complexity - O(n){Since we used set}
def findDuplicate(array):
    seen = set()
    for value in array:
        if value in seen:
            return value
        else:
            seen.add(value)
    return -1

## METHOD III using the fact that we can mutate the array and that values of elements in array are between 1 and len(arr) 
# Time Complexity - O(N), Space Complexity - O(1)
def findDuplicate(array):
    for value in array:
        absValue = abs(value)
        if array[absValue-1]<0:
            return absValue
        array[absValue-1] *= -1
    return -1

print(findDuplicate([1,5,2,5,7,9,4,3]))