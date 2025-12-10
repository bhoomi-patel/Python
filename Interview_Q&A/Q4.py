'''Implement binary search on a sorted list in Python, both iteratively and recursively. How would you handle cases where the target element appears multiple times?
Example:
List: [1, 3, 4, 6, 8, 9, 11, 15], Target: 6 → Index: 3
List: [2, 4, 4, 4, 7, 9], Target: 4 → First occurrence index: 1
'''
# Solution 1: Iterative Binary Search (Standard)
def binary_search_iterative(arr,target):
    left,right = 0,len(arr)-1
    while left<= right:
        mid = (left+right) //2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            left = mid +1
        else:
            left = mid -1
    return -1 # target not found

lst = [1, 3, 4, 6, 8, 9, 11, 15]
print(binary_search_iterative(lst, 6))  

# Solution 2: Recursive Binary Search
def binary_search_recursive(arr,target,left=0,right=None):
    if right is None:
        right = len(arr)-1
    if left>right:
        return -1
    mid = (left + right) //2
    if arr[mid]==target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example
print(binary_search_recursive([1, 3, 4, 6, 8, 9], 8))  # 4

# Solution 3: Binary Search for First Occurrence (Duplicates)
def binary_search_first_occurrence(arr,target):
    left , right = 0,len(arr) -1
    result = -1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target :
            result = mid
            right = mid -1
        elif arr[mid] <target:
            left = mid+1
        else:
            right = mid - 1
    return result
numbers = [2, 4, 4, 4, 7, 9]
print(binary_search_first_occurrence(numbers, 4))

# Solution 4: Using bisect Module (Built-in Utility)
import bisect

def binary_search_bisect(arr, target):
    idx = bisect.bisect_left(arr, target)
    if idx < len(arr) and arr[idx] == target:
        return idx
    return -1

# Example
numbers = [2, 4, 4, 4, 7, 9]
print(binary_search_bisect(numbers, 4)) 