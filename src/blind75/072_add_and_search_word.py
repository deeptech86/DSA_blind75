"""
Problem: Add and Search Word
Technique: Trie, DFS
"""

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # TODO: Implement initialization
        pass
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
        
        Args:
            word: str - Word to add
            
        Returns:
            None
        """
        # TODO: Implement addWord
        pass
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        
        Args:
            word: str - Word to search for
            
        Returns:
            bool - True if the word is in the data structure, False otherwise
        """
        # TODO: Implement search
        pass


# Example 1
# Input:
# ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
# [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]] 
# Output:
# [null, null, null, null, false, true, true, true]
# Explanation:
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True - matches "bad", "dad", "mad"
# wordDictionary.search("b.."); // return True - matches "bad"

# Example 2
# Input: 
# ["WordDictionary", "addWord", "search"]
# [[], ["hello"], ["hello"]]
# Output:
# [null, null, true]
# Explanation:
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("hello");
# wordDictionary.search("hello"); // returns True
