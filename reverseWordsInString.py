"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

def reverseWords(s: str) -> str:
    split = reversed(s.split()) # Split the string into an array, then reverse it
    return " ".join(split) # .join the reversed array to become a string again.