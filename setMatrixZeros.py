"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

"""

# Time: O(M x N), Space: O(M+N)
def setZeroes(self, matrix: List[List[int]]) -> None:
    i_store, j_store = set(), set() # Set to count which rows and cols to make 0
    # Iterate through matrix to look for 0 vals. Add those cols and rows to the store sets.
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 0:
                i_store.add(i)
                j_store.add(j)
    # Iterate through matrix again and if the row and col is in the store sets, set the val to 0.
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(row):
            if i in i_store or j in j_store:
                matrix[i][j] = 0

# Can do this in O(M x N) Time but with O(1) Space