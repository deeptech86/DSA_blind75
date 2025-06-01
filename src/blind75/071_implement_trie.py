"""
Problem: Implement Trie (Prefix Tree)
Technique: Trie
"""

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # TODO: Implement initialization
        pass
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        
        Args:
            word: str - Word to insert
            
        Returns:
            None
        """
        # TODO: Implement insertion
        pass
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        
        Args:
            word: str - Word to search for
            
        Returns:
            bool - True if the word is in the trie, False otherwise
        """
        # TODO: Implement search
        pass
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        
        Args:
            prefix: str - Prefix to search for
            
        Returns:
            bool - True if there is any word in the trie that starts with the given prefix, False otherwise
        """
        # TODO: Implement startsWith
        pass


# Example 1
# Input:
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output:
# [null, null, true, false, true, null, true]
# Explanation:
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // returns True
# trie.search("app");     // returns False
# trie.startsWith("app"); // returns True
# trie.insert("app");
# trie.search("app");     // returns True

# Example 2
# Input: 
# ["Trie", "insert", "search", "startsWith"]
# [[], ["hello"], ["hello"], ["hell"]]
# Output:
# [null, null, true, true]
# Explanation:
# Trie trie = new Trie();
# trie.insert("hello");
# trie.search("hello");   // returns True
# trie.startsWith("hell"); // returns True
