"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

"""

from collections import Counter

# Time: O(nlog(n)), Space: O(n)
def topKFrequent(words: List[str], k: int) -> List[str]:
    # Sort the Counter dictionary by the num of Occurances and if equal by lexicographical order.
    counts = dict(sorted(Counter(words).items(), key=lambda x: (-x[1],x))) 
    return list(counts.keys())[:k] # Return the K first keys (which are already sorted)

# Can also do in O(nlogk) Time using Heap.