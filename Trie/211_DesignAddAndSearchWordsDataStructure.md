## 211. Design Add and Search Words Data Structure
### Description

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.  
void addWord(word) Adds word to the data structure, it can be matched later.  
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.  

Example:  
Input  
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]  
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]  
Output  
[null,null,null,null,false,true,true,true]  

Explanation  
WordDictionary wordDictionary = new WordDictionary();  
wordDictionary.addWord("bad");  
wordDictionary.addWord("dad");  
wordDictionary.addWord("mad");  
wordDictionary.search("pad"); // return False  
wordDictionary.search("bad"); // return True  
wordDictionary.search(".ad"); // return True  
wordDictionary.search("b.."); // return True  

### Solution
* Use **Tire(Prefix Tree)**

```python
class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        if not word:
            return False
        return self.searchInNode(self.root, word, 0)
    
    def searchInNode(self, node, word, index):
        if not node:
            return False

        if index >= len(word):
            return node.isEnd
        
        char = word[index]
        if char != '.':
            if char not in node.children:
                return False
            return self.searchInNode(node.children[char], word, index+1)
        
        for c in node.children:
            if self.searchInNode(node.children[c], word, index+1):
                return True
        
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
