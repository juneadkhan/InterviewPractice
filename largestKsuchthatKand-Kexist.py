"""
Largest K such that both K and -K exist in array

[1, 2, 3, 4, 5, 6, -2, -5]

"""

"""
INPUT: list of integers (both + and -)
OUTPUT: an integer such that it and its - value exist in input list


"""

# Time: O(n), Space: O(n)
def largestK(arr):
    
    store = set(arr) # Make set out of array so we can check if it is in (O(1) Lookup)
    maxSoFar = float('-inf')
    
    for i in arr:
        if -i in store:
            maxSoFar = max(maxSoFar, i)
    
    return maxSoFar

print(largestK([1, 2, 3, 4, 5, 6, -2, -5]))
print(largestK([1,2,3,4,-1,-2,-3]))
print(largestK([]))
print(largestK([5,3,4]))
print(largestK([-5,-3,-4]))
