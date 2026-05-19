# #basics #math
# Print All Factors of a Given Number
# Source: Code & Debug - DSA Python Course Part 9
import math
from math import sqrt
from typing import List

def get_all_factors(n: int) -> List[int]:
    """
    Find all factors of a given number.

    Args:
        n: A positive integer

    Returns:
        A list of all factors in ascending order

    Example:
        get_all_factors(12) -> [1, 2, 3, 4, 6, 12]
    """
    # TODO: Implement your solution here
    nums=n
    result=[]
    for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                result.append(i)
                if (i != n//i):  # avoid duplicate for perfect square
                    result.append(n//i)
    return sorted(result)






def test_get_all_factors():
    # Test cases
    assert get_all_factors(12) == [1, 2, 3, 4, 6, 12]
    assert get_all_factors(1) == [1]
    assert get_all_factors(7) == [1, 7]  # Prime number
    assert get_all_factors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]
    assert get_all_factors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
    print("All test cases passed!")


if __name__ == "__main__":
    test_get_all_factors()
