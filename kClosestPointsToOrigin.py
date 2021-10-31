"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

"""

import math

# Time: O(nlogn), Space: O(1)
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    # Sort the points array by the distance, calculated using custom key + lambda function
    points.sort(key = lambda x : math.sqrt((x[0])**2 + (x[1])**2))
    return points[:k] # Return the first k elements of sorted array.