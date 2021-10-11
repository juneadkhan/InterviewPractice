"""
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3

"""

# Time: O(n), Space: O(n)
def lengthOfLongestSubstring(s: str) -> int:
    queue = deque()
    seen = set()
    longest = 0
    for i in s:
        if i in seen: # If i is in seen
            popped = None
            while popped != i:
                popped = queue.popleft() # Remove the first in the queue
                seen.remove(popped) # Remove that char from seem too
        # Now queue and seen represent everything from 2nd char to current.
        seen.add(i) # now add char i to end of queue and seen.
        queue.append(i)
        longest = max(longest, len(seen)) 
    return longest


# Time: O(n^2), Space: O(1)
def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    for i in range(len(s)+1):
        for j in range(1, len(s)+1):
            current = s[i:j]
            if len(set(current)) == len(current) and len(current) > longest:
                longest = len(current)
    return longest