## 14. Longest Common Prefix
### Description
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:  
Input: strs = ["flower","flow","flight"]  
Output: "fl"  
Example 2:  
Input: strs = ["dog","racecar","car"]  
Output: ""  
Explanation: There is no common prefix among the input strings.  

### Solution 1

#### Simulation
* Time Complexity: O(m * n)

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][:i]
    
        return strs[0]
```

#### Trie
* Time Complexity: O(S), S is the sum of the length of all strings

```python
class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()
        self.minLen = sys.maxsize
    
    def add(self, word):
        if not word:
            self.minLen = 0
            return False
        self.minLen = min(self.minLen, len(word))
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.isEnd = True
        return True
    
    def getCommonPrefix(self):
        prefix = []
        node = self.root
        for i in range(self.minLen):
            if len(node.children) > 1:
                break
            prefix += node.children.keys()
            node = node.children[prefix[-1]]
        return ''.join(prefix)
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        trie = Trie()
        idx_min_length = 0
        for i, word in enumerate(strs):
            if not trie.add(word):
                return ''
        
        return trie.getCommonPrefix()
```
