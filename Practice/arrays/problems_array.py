# 1 --> leetcode - two sum 
''' Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target. You may assume that each input will have exactly one solution. '''
# def twoSum(nums,target):
#     lookup= {}
#     for i , num in enumerate(nums):
#         remaining = target- num
#         if remaining in lookup:
#             return [lookup[remaining],i]
#         lookup[num] = i
#     return []

# print(twoSum([2,7,11,15],9))

# 2 --> HackerRank — Simple Array Sum
''' Given an array of integers, find the sum of its elements.'''
# def arr(ar):
#     return sum(ar)
# print(arr([1,2,3,4,10,11]))

# 3 --> leetcode - Best Time to Buy and Sell Stock
'''You have an array prices[], where prices[i] = stock price on day i.
Find the max profit you can achieve by choosing one buy day and one sell day (buy before sell).
If no profit → return 0.'''

# def maxProfit(prices):
#     min_price = float('inf')  # keep track of lowest price so far
#     max_profit = 0            # keep track of best profit
#     for i in prices :
#         min_price = min(min_price,i) 
#         max_profit = max(max_profit,i - min_price)
#     return max_profit
# print(maxProfit([7,1,5,3,6,4]))

# 4 --> HackerRank — Compare the Triplets

'''Description:
Alice and Bob each have 3 scores (triplets). Compare them:
If Alice’s score > Bob’s → Alice gets 1 point.
If Bob’s score > Alice’s → Bob gets 1 point.
If equal → no points.
Return [Alice_points, Bob_points].'''

# def compareTriplets(a, b):
#     alice = 0
#     bob = 0

#     for i in range(3):  # Compare each score
#         if a[i] > b[i]:
#             alice += 1
#         elif a[i] < b[i]:
#             bob += 1
#         # else: equal → no points

#     return [alice, bob]
# print(compareTriplets([5, 6, 7],[3, 6, 10]))

# 5 --> LeetCode — Move Zeroes (#283)
'''Description: Given an array nums, move all 0s to the end while keeping the relative order of non-zero elements. Do it in-place (no extra array). '''
# def moveZeroes(nums):
#     last_non_zero = 0  # pointer for where to put next non-zero

#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
#             last_non_zero += 1
#     return nums
# print(moveZeroes([0,1,0,3,12]))  # Output: [1,3,12,0,0]

# 6 --> HackerRank — Left Rotation
''' Description: Given an array a and number d, perform d left rotations → move first d elements to the end. '''
# def rotLeft(a, d):
#     n = len(a)
#     d = d % n  # Handle if d > n
#     return a[d:] + a[:d]
# print(rotLeft([1,2,3,4,5], 2))  # Output: [3,4,5,1,2]

# 7 --> LeetCode — Missing Number (#268)
'''Description: Given an array nums containing n distinct numbers taken from 0, 1, 2, ..., n, find the missing number. '''
# def missingNumber(nums):
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2  # Sum of 0..n
#     actual_sum = sum(nums)           # Sum of given array
#     return expected_sum - actual_sum
# print(missingNumber([3,0,1]))  # Output: 2

# 8 --> HackerRank — Diagonal Difference
'''Description: Given a square matrix (2D array) arr, calculate the absolute difference between the sums of its primary diagonal (top-left → bottom-right) and secondary diagonal (top-right → bottom-left).
arr = [
 [11, 2, 4],
 [4, 5, 6],
 [10, 8, -12]
]
# Primary diagonal: 11 + 5 + (-12) = 4
# Secondary diagonal: 4 + 5 + 10 = 19
# Difference = |4 - 19| = 15'''
# def diagonalDifference(arr):
#     n = len(arr)
#     primary = 0
#     secondary = 0

#     for i in range(n):
#         primary += arr[i][i]           # Top-left → bottom-right
#         secondary += arr[i][n-1-i]     # Top-right → bottom-left

#     return abs(primary - secondary)
# print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))  # Output: 15

# 9 --> LeetCode — Maximum Subarray (#53)
''' Description: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.'''
# def maxSubArray(nums):
#     max_current = max_global = nums[0]  # Start with first element

#     for i in range(1, len(nums)):
#         # Either extend current subarray or start new from current element
#         max_current = max(nums[i], max_current + nums[i])
#         # Update global max
#         if max_current > max_global:
#             max_global = max_current

#     return max_global
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6 (subarray [4,-1,2,1])

# 10 --> HackerRank — Ice Cream Parlor
''' Description: Given an array cost[] and money, find two distinct flavors whose cost sums exactly to money. Return 1-based indices. '''
# def icecreamParlor(money, cost):
#     lookup = {}  # cost : index

#     for i, c in enumerate(cost):
#         diff = money - c
#         if diff in lookup:
#             return [lookup[diff]+1, i+1]  # 1-based index
#         lookup[c] = i
#     return []
# print(icecreamParlor(4, [1, 4, 5, 3, 2]))  # Output: [1, 4]


# 11 → LeetCode — Find All Duplicates (#442)

''' Description:
Given an array of integers nums where 1 ≤ nums[i] ≤ n (n = size of array), some elements appear twice. Find all elements that appear twice. Do it in O(n) time and O(1) extra space (modifying the array is allowed). '''
# def findDuplicates(nums):
#     result = []
#     for num in nums:
#         index = abs(num) - 1  # Map number to index
#         if nums[index] < 0:
#             result.append(abs(num))  # Already visited → duplicate
#         else:
#             nums[index] = -nums[index]  # Mark as visited
#     return result

# print(findDuplicates([4,3,2,7,8,2,3,1]))  # Output: [2,3]

# 12 → LeetCode — Majority Element (#169)

''' Description:
Given an array of size n, find the element that appears more than n/2 times. '''
# def majorityElement(nums):
#     count = 0
#     candidate = None

#     for num in nums:
#         if count == 0:
#             candidate = num
#         count += (1 if num == candidate else -1)

#     return candidate

# print(majorityElement([3,2,3]))  # Output: 3

# 13 → LeetCode — Rotate Array (#189)
''' Description: Rotate array nums to the right by k steps, where k is non-negative. '''
# ex:  Input: [1,2,3,4,5,6,7], k = 3
#      Output: [5,6,7,1,2,3,4]
# def rotate(nums, k):
#     n = len(nums)
#     k %= n  # In case k > n

#     # Reverse entire array
#     nums[:] = nums[::-1]
#     # Reverse first k elements
#     nums[:k] = nums[:k][::-1]
#     # Reverse remaining
#     nums[k:] = nums[k:][::-1]
#     return nums

# print(rotate([1,2,3,4,5,6,7], 3))  # Output: [5,6,7,1,2,3,4]

# 14 → LeetCode — Container With Most Water (#11)

''' Description:
Given height[], find two lines that together with x-axis forms container with most water. Return max area. '''
# def maxArea(height):
#     left, right = 0, len(height)-1
#     max_area = 0

#     while left < right:
#         width = right - left
#         area = min(height[left], height[right]) * width
#         max_area = max(max_area, area)

#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1

#     return max_area

# print(maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49

# 15 → LeetCode — Subarray Sum = K (#560)

# Description:
''' Given array nums and k, find total number of continuous subarrays whose sum = k. '''
# def subarraySum(nums, k):
#     count = 0
#     curr_sum = 0
#     lookup = {0:1}  # sum: frequency

#     for num in nums:
#         curr_sum += num
#         if curr_sum - k in lookup:
#             count += lookup[curr_sum - k]
#         lookup[curr_sum] = lookup.get(curr_sum,0) + 1

#     return count

# print(subarraySum([1,1,1],2))  # Output: 2

# 16 → HackerRank — Counting Sort
''' Description: Given an array of integers arr where each integer is between 0 and 100, return the frequency count of each integer.'''
# def countingSort(arr):
#     count = [0]*101  # For 0..100
#     for num in arr:
#         count[num] += 1
#     return count

# print(countingSort([1,1,3,2,1]))  # Output: [0,3,1,1,0,...]

#  17 → HackerRank — Mini-Max Sum
''' Description: Given 5 positive integers, calculate minimum sum (sum of 4 smallest) and maximum sum (sum of 4 largest)''' 
# def miniMaxSum(arr):
#     total = sum(arr)
#     min_sum = total - max(arr)
#     max_sum = total - min(arr)
#     return min_sum, max_sum

# print(miniMaxSum([1,2,3,4,5]))  # Output: (10,14)

# 18 → HackerRank — Subarray Division (Birthday Chocolate)
''' Description:
Given squares of chocolate and a day d and month m, find number of contiguous segments of length m with sum = d.

Example:

s = [1,2,1,3,2], d = 3, m = 2
Output: 2  # [1,2] and [2,1] '''

# def birthday(s, d, m):
#     count = 0
#     for i in range(len(s) - m + 1):
#         if sum(s[i:i+m]) == d:
#             count += 1
#     return count

# print(birthday([1,2,1,3,2],3,2))  # Output: 2

# 19 -->  HackerRank — Migratory Birds
''' Description:
Given array of bird sightings arr with types 1..5, find most frequent bird type. If tie, return smallest id.

Example:

arr = [1,1,2,2,3]
Output: 1 '''
# def migratoryBirds(arr):
#     count = [0]*6  # Index 0 unused
#     for bird in arr:
#         count[bird] += 1
#     max_count = max(count)
#     return count.index(max_count)

# print(migratoryBirds([1,1,2,2,3]))  # Output: 1

# 20 → HackerRank — Array Manipulation
''' Description:
Given n zeros array and queries of form [a,b,k], add k to all elements from a to b (1-indexed). Return max value after all operations.

Example:

n = 5, queries = [[1,2,100],[2,5,100],[3,4,100]]
Output: 200 '''
# def arrayManipulation(n, queries):
#     arr = [0]*(n+1)
#     for a,b,k in queries:
#         arr[a-1] += k
#         arr[b] -= k  # Subtract after end index

#     max_val = 0
#     curr = 0
#     for num in arr:
#         curr += num
#         max_val = max(max_val, curr)
#     return max_val

# print(arrayManipulation(5, [[1,2,100],[2,5,100],[3,4,100]]))  # Output: 200
