"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""

# O(n) Time, O(n) Space
def isPalindrome(s: str) -> bool:
    string = ''.join([x.lower() for x in s if x.isalnum()])
    return string == string[::-1]