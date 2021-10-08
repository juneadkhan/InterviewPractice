"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.
"""


import collections

# O(n) Time, O(n) Space
def findDuplicate(nums):
    counts = collections.Counter(nums)
    for i in counts:
        if counts[i] != 1:
            return i
