"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true
"""

# O(n) Time, O(n) Space
def isValid(s: str) -> bool:
    print(s)
    pairs = {"{" : "}", "(" : ")", "[" : "]"}
    stack = []
    for i in s:
        if i in {"{", "(", "["}:  
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            x = stack.pop()
            if pairs[x] != i: # Last seen opening bracket must match first closing bracket.
                return False
    if stack:
        return False
    else:
        return True