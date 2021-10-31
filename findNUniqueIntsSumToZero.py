"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

"""

# Time: O(n), Space: O(1)
def sumZero(n: int) -> List[int]:
    
    out = []
    
    # Append a + and - version of a number until you reach n for even or n - 1 for odd.
    for i in range(1,n,2):
            out.append(i)
            out.append(-i)
    
    # If odd number, append an extra 0.
    if n % 2 != 0:
        out.append(0)
        
    return out
