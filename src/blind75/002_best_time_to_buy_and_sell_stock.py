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
    min_price=prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price= price
        else:
            current_profit = price - min_price
            max_profit =max(current_profit, max_profit)
    return max_profit



# Example 1
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5

# Example 2
# Input: prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: No transactions are done (i.e., max profit = 0)


prices = [7, 6, 4, 3, 1]
print(best_time_to_buy_and_sell_stock(prices))