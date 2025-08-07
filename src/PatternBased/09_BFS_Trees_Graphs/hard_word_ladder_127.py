"""
LeetCode 127: Word Ladder
Difficulty: Hard
Pattern: BFS - Graphs

A transformation sequence from word beginWord to word endWord using a dictionary wordList 
is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of 
words in the shortest transformation sequence from beginWord to endWord, or 0 if no such 
sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord != endWord
- All the strings in wordList are unique.
"""

def ladderLength(beginWord, endWord, wordList):
    """
    Time Complexity: O(M² * N) where M is length of each word and N is total number of words
    Space Complexity: O(M² * N)
    
    TODO: Implement the solution using BFS with word transformations
    Hint: Use BFS to find shortest path, create patterns for one-letter changes
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("hit", "cog", ["hot","dot","dog","lot","log","cog"]),
        ("hit", "cog", ["hot","dot","dog","lot","log"]),
        ("a", "c", ["a","b","c"]),
        ("hot", "dog", ["hot","dog"])
    ]
    
    for beginWord, endWord, wordList in test_cases:
        result = ladderLength(beginWord, endWord, wordList)
        print(f'beginWord: "{beginWord}", endWord: "{endWord}"')
        print(f"wordList: {wordList}")
        print(f"Shortest transformation length: {result}\n")
