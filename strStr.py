"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Input: haystack = "hello", needle = "ll"
Output: 2

"""

# Time: O(n), Space: O(1)
def strStr(haystack: str, needle: str) -> int:
    # Check if needle in haystack. if it is, return the index it begins at, otherwise return -1.
    return haystack.index(needle) if needle in haystack else -1
    
        