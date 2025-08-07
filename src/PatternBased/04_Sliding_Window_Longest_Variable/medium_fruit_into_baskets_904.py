"""
LeetCode 904: Fruit Into Baskets
Difficulty: Medium
Pattern: Sliding Window (Longest Variable Window)

You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] is the type of 
fruit the ith tree produces. You want to collect as much fruit as possible. However, 
the owner has some strict rules that you must follow:
- You only have two baskets, and each basket can only hold a single type of fruit.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree 
  (including the start tree) while moving to the right.

Example:
Input: fruits = [1,2,1]
Output: 3

Constraints:
- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length
"""

def totalFruit(fruits):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using sliding window technique
    Hint: Think of this as "longest subarray with at most 2 distinct elements"
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 2, 1],
        [0, 1, 2, 2],
        [1, 2, 3, 2, 2],
        [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    ]
    
    for fruits in test_cases:
        result = totalFruit(fruits)
        print(f"Fruits: {fruits}")
        print(f"Maximum fruits: {result}\n")
