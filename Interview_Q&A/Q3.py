'''Write a function to check if two strings are anagrams of each other. Handle edge cases like spaces and different cases.
Example:
"Listen" and "Silent" → True
"The Morse Code" and "Here come dots" → True
"Hello" and "World" → False
[in short- Compare if two strings contain the same characters with same frequency]
'''
# Solution 1: Using sorted() (Most Common)
def anagram_count(str1,str2):
    # remove space and convert to lowercase
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    # compare sorted strings
    return sorted(str1) == sorted(str2)
print(anagram_count("listen","silent"))
print(anagram_count("hello","World"))

# Solution 2: Using collections.Counter (Recommended)
from collections import Counter

def anagrams_counter(str1, str2):
    return Counter(str1) == Counter(str2)

# Example
print(anagrams_counter("listen", "silent"))

# Solution 3: Sorting Strings
def anagrams_sort(str1,str2):
    return sorted(str1) == sorted(str2)
print(anagrams_sort("sort","rost"))