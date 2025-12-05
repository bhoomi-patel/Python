'''How would you find and remove all duplicates from a Python list while preserving the original order of elements?

Given a list: [1, 3, 2, 1, 5, 3, 2, 6, 8, 5]
Expected output: [1, 3, 2, 5, 6, 8]'''

# Solution 1: Using dict.fromkeys() (Recommended)
lst = [1, 3, 2, 1, 5, 3, 2, 6, 8, 5]
def remove_duplicate(lst):
    return list(dict.fromkeys(lst))
result = remove_duplicate(lst)
print("Using Dict :-",result)

# Solution 2 : Set
print("Using set-",list(set(lst)))

# Solution 3: Using OrderedDict (Python < 3.7)
from collections import OrderedDict
def remove_duplicate_ordered(lst):
    return list(OrderedDict.fromkeys(lst))
result = remove_duplicate(lst)
print("Using OrderedDict :-",result)   