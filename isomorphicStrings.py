"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

"""

# O(n) time, O(1) space (size of ASCII character space is fixed)

def isIsomorphic(s: str, t: str) -> bool:
    s_to_t = {} # Use two way mapping dictionaries to confirm mappings are same both directions
    t_to_s = {}
    
    for i in range(len(s)):
        if s[i] not in s_to_t and t[i] not in t_to_s:
            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]
        if s[i] not in s_to_t or t[i] not in t_to_s:
            return False
        if s_to_t[s[i]] != t[i] or t_to_s[t[i]] != s[i]:
            return False
    return True