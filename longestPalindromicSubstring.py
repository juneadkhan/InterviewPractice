"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

"""

# Time: O(n^2), Space: O(1)
def longestPalindrome(self, s: str) -> str:
    result = ""
    # Iterate through each character in the string
    for i in range(len(s)):
        # Check Odd Cases
        left, right = i, i # Start from the center of the current Char. Expand Outwards
        # Keep iterating as long as left and right within bounds of string
        # and the substring is a palindorme denoted by: s[left] == s[right]
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len(result):
                result = s[left:right+1]
            # Expand Outwards
            left -= 1
            right += 1
        
        # Check Even Cases
        left, right = i, i+1 # Start from the center of the current Char. Exapnd outwards
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len(result):
                result = s[left:right+1]
            # Expand Outwards
            left -= 1
            right += 1
            
    return result
        