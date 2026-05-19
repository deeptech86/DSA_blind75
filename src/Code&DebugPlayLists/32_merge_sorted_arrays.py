# #array #two_pointers
# Merge 2 Sorted Arrays Without Duplicates
# Source: Code & Debug - DSA Python Course Part 32

from typing import List

def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Merge two sorted arrays into one sorted array without duplicates.

    Args:
        arr1: First sorted list of integers
        arr2: Second sorted list of integers

    Returns:
        Merged sorted list without duplicates

    Example:
        merge_sorted_arrays([1, 3, 5], [2, 3, 6]) -> [1, 2, 3, 5, 6]
    """
    # TODO: Implement your solution here
    n=len(arr1)
    m=len(arr2)
    # result_arr=[]
    filter_dict={}

    for i in range(n):
        if arr1[i] not in filter_dict:
            filter_dict[arr1[i]]=0
    for j in range(m):
        if arr2[j] not in filter_dict:
            filter_dict[arr2[j]]=0
    result_arr = list(filter_dict.keys())
    result_arr.sort()

    # print(result_arr.sort())
    return result_arr









def test_merge_sorted_arrays():
    # Test cases
    assert merge_sorted_arrays([1, 3, 5], [2, 3, 6]) == [1, 2, 3, 5, 6]
    assert merge_sorted_arrays([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_arrays([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_arrays([1, 1, 1], [1, 1, 1]) == [1]
    assert merge_sorted_arrays([1, 2], [2, 3]) == [1, 2, 3]
    print("All test cases passed!")


if __name__ == "__main__":
    test_merge_sorted_arrays()
