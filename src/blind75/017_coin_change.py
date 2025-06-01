"""
Problem: Coin Change
Technique: Dynamic Programming (Knapsack)
"""

def coin_change(coins, amount):
    """
    You are given an integer array coins representing coins of different denominations
    and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount.
    
    Args:
        coins: List[int] - Array of coin denominations
        amount: int - Target amount
        
    Returns:
        int - Fewest number of coins needed, or -1 if not possible
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2
# Input: coins = [2], amount = 3
# Output: -1
# Explanation: It's not possible to make 3 with only coin of value 2
