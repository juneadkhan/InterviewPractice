"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Input: s = "anagram", t = "nagaram"
Output: true
"""

# O(n) Solution:
def isAnagram(s, t):
    return sorted(s) == sorted(t)