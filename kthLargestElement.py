"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

"""

# O(n) Time, O(1) Space
def findKthLargest(nums: List[int], k: int) -> int:
    heapq._heapify_max(nums) # Turn nums array into MaxBinHeap
    for i in range(k):
        # Perform K pops of max of BinHeap to get Kth Max.
        maxi = heapq._heappop_max(nums) # O(1) to get max of BinHeap. 
    return maxi