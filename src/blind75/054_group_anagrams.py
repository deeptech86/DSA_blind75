"""
Problem: Group Anagrams
Technique: Hash Table
"""
from collections import defaultdict


def group_anagrams(strs):
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    
    Args:
        strs: List[str] - Array of strings
        
    Returns:
        List[List[str]] - Grouped anagrams
    """
    # TODO: Implement solution
    # dict = defaultdict(list)
    # grouped=[]
    # for each_str in strs:
    #     sorted_s = "".join(sorted(each_str))
    #     # if sorted(each_str) not in dict.values():
    #     dict[sorted(each_str)].append(each_str)
    # return list(dict.values())

    sMap = defaultdict(list)

    for s in strs:
        sorted_s = "".join(sorted(s))
        sMap[sorted_s].append(s)

    return list(sMap.values())





# Example 1
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# Explanation: The words that are anagrams of each other are grouped together

# Example 2
# Input: strs = [""]
# Output: [[""]]
# Explanation: There is only one word, which forms its own group
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))