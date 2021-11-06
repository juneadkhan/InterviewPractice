"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

"""

class Solution:
    # Time: O(s + t)
    def minWindow(self, s: str, t: str) -> str:
        """
        INPUT: 2 strings. S is the string we want to find a substring in. t is the chracters the substring must contain
        
        OUTPUT: string, is the minimum window substring. String of smallest length which contains all chracters from t
        
        """
        
        counts_of_t = Counter(t) 
            
        left = 0 
        
        no_t_in_s = 0 
        
        out = ''
        
        # Expanding from right
        for right in range(len(s)):
            
            if counts_of_t[s[right]] > 0 :
                no_t_in_s +=1
            
            
            counts_of_t[s[right]] -= 1
            

            # Contracting from left
            while no_t_in_s == len(t):
                # If out is empty or current window size is smaller than out size
                if not out or right-left+1 < len(out):
                    # Update out to be string defined by the new window.
                    out = s[left:right+1]

                counts_of_t[s[left]] +=1
                
                if counts_of_t[s[left]] > 0:
                    no_t_in_s -= 1
                
                # Contracts inwards from the left
                left += 1
        return out
        