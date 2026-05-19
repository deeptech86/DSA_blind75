# #array #dynamic_programming
# LeetCode 121: Best Time to Buy and Sell Stock
# Source: Code & Debug - DSA Python Course Part 37

from typing import List

def max_profit(prices: List[int]) -> int:
    """
    Find the maximum profit from buying and selling a stock once.

    Args:
        prices: List of stock prices where prices[i] is the price on day i

    Returns:
        Maximum profit possible, or 0 if no profit can be made

    Example:
        max_profit([7, 1, 5, 3, 6, 4]) -> 5
        (Buy on day 2 at price 1, sell on day 5 at price 6)
    """
    # TODO: Implement your solution here
    pass


def test_max_profit():
    # Test cases
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1, 2]) == 1
    assert max_profit([2, 1]) == 0
    assert max_profit([1]) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_max_profit()
