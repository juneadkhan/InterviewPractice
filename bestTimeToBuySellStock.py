"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""
# Sliding Window Solution
# Time: O(n), Space: O(1) 
def maxProfit(prices: List[int]) -> int:
    maxProfit = 0
    buy = 0 # Start Buy at 0th Index and Sell at 1st Index.
    # Iterate through all the prices
    for sell in range(1, len(prices)):
        # Calculate the profit 
        profit = prices[sell] - prices[buy]
        # If the profit is negative, move the buy index up to the current sell index.
        if profit < 0:
            buy = sell
        # Update maxProfit if the current profit is greater
        if profit > maxProfit:
            maxProfit = profit
    return maxProfit