"""
Given an amount and the denominations of coins available, determine how many ways change can be made for amount.
There is a limitless supply of each coin type.
"""

def getWays(num, coins):
    """
    1. 0 Column always 1 since you can make 0 out of no coins. That is 1 way.
    2. table[col][row] = table[col][row-1] + table[col - coins[row-1]]
    
            | 0 | 1 | 2 | 3 | 4 | 
    ---------------------------------
    []      | 1 | 0 | 0 | 0 | 0 |
    [1]     | 1 | 1 | 1 | 1 | 1 |
    [1,2]   | 1 | 1 | 2 | 2 | 3 | 
    [1,2,3] | 1 | 1 | 2 | 3 | 4 |
    """
    # Make Blank 2D Array representing coin denominations and sums
    data = [0] * (num+1) # Create num+1 Columns. when num = 4, make 5 cols
    for i in range(num+1):
        data[i] = [0] * (len(coins) + 1) # Make num of coins + 1 rows. accounts for []
        
    for i in range(0, len(coins)+1): 
        data[0][i] = 1 # Fill out first column with all 1s. Always 1 way to make zero for all denominations.
        
    for i in range(1, num+1):
        data[i][0] = 0 # Other than [0,0], you can't make any other n with no coins.
        for j in range(1, len(coins)+1): # Consider for J coin types
            value = data[i][j-1] # Possibe ways when we can't use the Jth coin.
    
            if coins[j-1] <= i: # Cant make a number with coin if coin > number. E.g can't make 4p with 5p coin.
                value += data[i - coins[j-1]][j] # All Possible ways using the Jth coin

            data[i][j] = value # table[col][row] = table[col][row-1] + table[col - coins[row-1]]
                
    return data[num][len(coins)] # Return bottom right answer. Number of ways to make num with all the coins.