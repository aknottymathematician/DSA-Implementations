"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

##METHOD I(2 for loops) 
## Time Complexity O(N^2), Space Complexity O(1)
def twoSumsfor(arr, target):
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            if arr[i]+arr[j] == target:
                return [i, j]
    return []



##METHOD II(Hash Tables)
## Time Complexity O(N), Space Complexity O(N){For extra use of Hash tables}
def twoSumshash(arr, target):
    nums={}
    for num in arr:
        pot_num = target-num
        if pot_num in nums:
            return [pot_num, num]
        else:
            nums[num]=True
    return []


##METHOD III(Sort the array)
## Time Complexity O(NlogN), Space Complexity O(1)
def twoSumsort(arr, target):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left<right:
        if arr[left]+arr[right] == target:
            return [left, right]
        elif arr[left]+arr[right] < target:
            left += 1
        elif arr[left]+arr[right] > target:
            right -= 1
    return []

print(twoSumsort([2,7,11,15], 18))