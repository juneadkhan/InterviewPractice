"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

"""

from itertools import groupby
import collections

# Time: O(n), Space: O(n)
def compress(chars: List[str]) -> int:
    out = []
    consGrouped = [list(g) for k,g in groupby(chars)]
    for i in consGrouped:
        out.append(str(i[0]))
        if len(i) > 1:
            for j in str(len(i)):
                out.append(j)
    chars[:] = out
    return len(out)

