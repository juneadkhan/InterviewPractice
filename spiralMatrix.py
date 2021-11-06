"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        INPUT: 2D-Array (m x n)
        OUTPUT: Array of elements in Spiral Order
        
        X. Start at the top-left
        
        1. Go right until you reach the rightmost. M  M-1
        2. Go Down until you reach the bottom most. N N-2
        3. Go left until you reach the left most. M
        4. Go Up until you reach the top most N-1
        
        queue. the values
        
        """
        x, y = 0 , 0
        tl, tr, br, bl = 0, len(matrix[0]), len(matrix), -1
                
        queue = []
        
        # Up, Down, Left, Right, Stop
        flag = "Right"
        
        while flag != "Stop":
            if len(queue) == len(sum(matrix, [])):
                return queue
            if flag == "Right":
                if x == tr:
                    flag = "Down"
                    x -= 1
                    y += 1
                    tr -= 1
                else:
                    queue.append(matrix[y][x])
                    x += 1
                    
            if flag == "Down":
                if y == br:
                    flag = "Left"
                    y -= 1
                    x -= 1
                    br -= 1
                else:
                    queue.append(matrix[y][x])
                    y += 1
                    
            if flag == "Left":
                if x == bl:
                    flag = "Up"
                    x += 1
                    y -= 1
                    bl += 1
                else:
                    queue.append(matrix[y][x])
                    x -= 1
                    
            if flag == "Up":
                if y == tl:
                    flag = "Right"
                    y += 1
                    x += 1
                    tl += 1
                else:
                    queue.append(matrix[y][x])
                    y -= 1