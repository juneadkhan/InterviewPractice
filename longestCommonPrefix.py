"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstString = strs[0] # Take the first value in the list
        currentLongest = "" # Keep track of the current longest

        for i in range(0,len(firstString)+1): # For each character of the first string
            for str in strs: # Check each word in the list

                if firstString[0:i] != str[0:i]: # Check if the first i characters of the first string and current str are the same
                    return currentLongest # If they are not, the existing current longest is the current longest
                else:
                    currentLongest = firstString[0:i-1] # if the first i chars are the same, the current longest increased a character.
        return firstString