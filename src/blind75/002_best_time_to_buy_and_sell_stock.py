"""
Problem: Best Time to Buy and Sell Stock
Technique: Prefix Sum, Dynamic Programming
"""

def best_time_to_buy_and_sell_stock(prices):
    """
    Given an array prices where prices[i] is the price of a given stock on the ith day,
    find the maximum profit by buying on one day and selling on a future day.
    
    Args:
        prices: List[int] - Array of stock prices
        
    Returns:
        int - Maximum profit
    """
    # TODO: Implement solution
    start =0

    while start<len(prices)-1:
        if prices[start]> prices[start+1]:
            start+=1
            max_price = max(prices[start:])
            if prices.index(max_price) > start:
                return max_price - prices[start]



# Example 1
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5

# Example 2
# Input: prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: No transactions are done (i.e., max profit = 0)
