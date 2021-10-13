"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

"""

import heapq
from collections import Counter

# Time: O(n), Space: O(n)
def topKFrequent(nums: List[int], k: int) -> List[int]:
    counts = Counter(nums) # Count occurences for each num
    return [i for i,j in counts.most_common(k)] # Return the keys of the k most common elements
        
# Time: O(n), Space: O(n)
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counts = Counter(nums) # Count occurences for each num
    heap = []
    for key, value in counts.items():
        heapq.heappush(heap, (value, key)) 
    out = []
    klargest = heapq.nlargest(k, heap)
    for _, j in klargest:
        out.append(j)
    return out