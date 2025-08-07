# LeetCode Problems by Patterns

This directory contains LeetCode problems organized by algorithmic patterns. Each pattern has its own folder with multiple problems ranging from easy to hard difficulty (80% easy-medium, 20% hard).

## Directory Structure

```
PatternBased/
├── 01_Two_Pointers_Same_Direction/
├── 02_Two_Pointers_Opposite_Direction/
├── 03_Sliding_Window_Fixed/
├── 04_Sliding_Window_Longest_Variable/
├── 05_Sliding_Window_Shortest_Variable/
├── 06_Fast_Slow_Pointers/
├── 07_Prefix_Sum/
├── 08_Binary_Search/
├── 09_BFS_Trees_Graphs/
├── 10_DFS_Trees_Graphs/
└── README.md
```

## Pattern Overview

### 1. Two Pointers - Same Direction
**Use when:** Processing array elements in same direction with two pointers
**Problems:**
- Easy: Remove Duplicates from Sorted Array (26), Remove Element (27), Move Zeroes (283)
- Medium: Remove Duplicates from Sorted Array II (80)
- Hard: Trapping Rain Water (42)

### 2. Two Pointers - Opposite Direction
**Use when:** Need to find pairs/combinations by moving pointers from both ends
**Problems:**
- Easy: Two Sum II (167), Valid Palindrome (125)
- Medium: 3Sum (15), 3Sum Closest (16)
- Hard: Median of Two Sorted Arrays (4)

### 3. Sliding Window (Fixed Window)
**Use when:** Need to process subarrays of fixed size
**Problems:**
- Easy: Maximum Average Subarray I (643)
- Medium: Maximum Number of Vowels in Substring (1456), Max Consecutive Ones III (1004), Find All Anagrams in String (438)
- Hard: Sliding Window Maximum (239)

### 4. Sliding Window - (Longest Variable Window)
**Use when:** Finding the longest subarray/substring that satisfies a condition
**Problems:**
- Medium: Longest Substring Without Repeating Characters (3), Longest Repeating Character Replacement (424), Fruit Into Baskets (904)
- Hard: Minimum Window Substring (76)

### 5. Sliding Window - (Shortest Variable Window)
**Use when:** Finding the shortest subarray/substring that satisfies a condition
**Problems:**
- Medium: Minimum Size Subarray Sum (209), Longest Substring with At Most K Distinct Characters (340)
- Hard: Shortest Subarray with Sum at Least K (862)

### 6. Fast and Slow Pointers (Floyd's Cycle Detection)
**Use when:** Detecting cycles or finding middle elements
**Problems:**
- Easy: Linked List Cycle (141), Middle of Linked List (876), Happy Number (202)
- Medium: Linked List Cycle II (142), Find Duplicate Number (287)

### 7. Prefix Sum
**Use when:** Need to calculate range sums efficiently
**Problems:**
- Easy: Range Sum Query - Immutable (303), Find Pivot Index (724)
- Medium: Subarray Sum Equals K (560), Subarray Sums Divisible by K (974)
- Hard: Count of Range Sum (327)

### 8. Binary Search
**Use when:** Searching in sorted arrays or search spaces
**Problems:**
- Easy: Binary Search (704), Search Insert Position (35)
- Medium: Search in Rotated Sorted Array (33), Find Minimum in Rotated Sorted Array (153)
- Hard: Median of Two Sorted Arrays (4)

### 9. BFS - Trees / Graphs
**Use when:** Need level-order traversal or shortest path in unweighted graphs
**Problems:**
- Easy: Minimum Depth of Binary Tree (111)
- Medium: Binary Tree Level Order Traversal (102), Number of Islands (200), Rotting Oranges (994)
- Hard: Word Ladder (127)

### 10. DFS - Trees / Graphs
**Use when:** Need to explore all paths or validate tree properties
**Problems:**
- Easy: Maximum Depth of Binary Tree (104), Invert Binary Tree (226)
- Medium: Validate Binary Search Tree (98), Word Search (79)
- Hard: Binary Tree Maximum Path Sum (124)

## How to Use

1. **Identify the Pattern**: Look at the problem statement and identify which pattern it follows
2. **Study the Template**: Each file contains a template solution with time/space complexity analysis
3. **Practice Variations**: Start with easy problems and progress to harder ones within each pattern
4. **Run Tests**: Each file includes test cases to verify your understanding

## Key Learning Points

### Time Complexity Patterns:
- **Two Pointers**: O(n)
- **Sliding Window**: O(n)
- **Fast/Slow Pointers**: O(n)
- **Prefix Sum**: O(n) preprocessing, O(1) queries
- **Binary Search**: O(log n)
- **BFS**: O(V + E) for graphs, O(n) for trees
- **DFS**: O(V + E) for graphs, O(n) for trees

### Space Complexity Patterns:
- **Two Pointers**: O(1)
- **Sliding Window**: O(k) where k is window constraint
- **Fast/Slow Pointers**: O(1)
- **Prefix Sum**: O(n)
- **Binary Search**: O(1) iterative, O(log n) recursive
- **BFS**: O(w) where w is maximum width
- **DFS**: O(h) where h is maximum height/depth

## Problem Distribution

- **Easy**: 40% (Foundation building)
- **Medium**: 40% (Core interview problems)
- **Hard**: 20% (Advanced concepts)

## Tips for Success

1. **Master the Template**: Understand the basic template for each pattern
2. **Practice Edge Cases**: Always consider empty inputs, single elements, etc.
3. **Optimize Gradually**: Start with brute force, then optimize using patterns
4. **Trace Through Examples**: Walk through the algorithm step by step
5. **Time Yourself**: Practice solving problems within interview time constraints

## Next Steps

After completing these patterns, consider studying:
- Dynamic Programming patterns
- Graph algorithms (Dijkstra, Union-Find)
- Advanced data structures (Trie, Segment Tree)
- Backtracking patterns
- Greedy algorithms

Happy coding! 🚀
