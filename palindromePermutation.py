"""
Given a string, determine if a permutation of the string could form a palindrome.

For example, "code" -> False, "aab" -> True, "carerac" -> True.
"""

from collections import Counter

# Time: O(n), Space: O(n)
def canPermutatePalindrome1(str):
  counts = Counter(str) # Count occurence of each letter
  vals = [x for x in counts.values() if x % 2 != 0] # make list of only odd occuring letters
  return False if len(vals) > 1 else True # If more than 1 odd occuring letter, than it cannot be a Palindrome

# Time: O(n), Space: O(1) -> Worst Case set has all 26 unique chars.
def canPermutatePalindrome2(input):
  odd = set() # Stores values with odd num of occurences
  for char in input:
    if char in odd: # if char already in odd, another sighting will make it even, thus it can be removed.
      odd.remove(char)
    else:
      odd.add(char) # If already in odd, this will be an odd sighting.
  return len(odd) < 2 # If more than 1 odd occuring letter, than it cannot be a Palindrome

canPermutatePalindrome1("code")
canPermutatePalindrome1("aab")
canPermutatePalindrome1("carerac")

canPermutatePalindrome2("code")
canPermutatePalindrome2("aab")
canPermutatePalindrome2("carerac")