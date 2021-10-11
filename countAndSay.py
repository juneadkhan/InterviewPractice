"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

https://leetcode.com/problems/count-and-say/

"""

import collections
from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return say(self.countAndSay(n-1))
    
def say(word):
    out = []
    grouped = [list(g) for k, g in groupby(word)] # Splits list into similar consecutive characters. e.g. ['1211'] -> [['1'],['2'],['1','1']]
    for i in grouped:
        count = 0
        val = ''
        for j in i:
            val = j
            count += 1
        out.append(str(count))
        out.append(str(val))
    return "".join(out)
        