## 737. Sentence Similarity II

### Description
We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].

Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.

Return true if sentence1 and sentence2 are similar, or false if they are not similar.

Two sentences are similar if:

They have the same length (i.e., the same number of words)
sentence1[i] and sentence2[i] are similar.
Notice that a word is always similar to itself, also notice that the similarity relation is transitive. For example, if the words a and b are similar, and the words b and c are similar, then a and c are similar.

Example 1:  
Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [  ["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]  
Output: true  
Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the   corresponding word in sentence2.  

Example 2:  
Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]  
Output: true  
Explanation: "leetcode" --> "platform" --> "anime" --> "manga" --> "onepiece".  
Since "leetcode is similar to "onepiece" and the first two words are the same, the two sentences are similar.  

Example 3:  
Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]  
Output: false  
Explanation: "leetcode" is not similar to "onepiece".  

### Solution

```python
class UnionFind:
    def __init__(self, n):
        self.parents = [*range(n+1)]
        self.ranks = [0] * (n+1)
    
    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        elif self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        else:
            self.parents[px] = py
            self.ranks[py] += 1

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        m, n = len(sentence1), len(sentence2)
        if m != n or not similarPairs:
            return False
        
        uf = UnionFind(len(similarPairs)*2)
        self.wordDict = {}
        
        for w1, w2 in similarPairs:
            uf.union(self.getIndex(w1), self.getIndex(w2))
        
        for i in range(m):
            w1, w2 = sentence1[i], sentence2[i]
            if uf.find(self.getIndex(w1)) != uf.find(self.getIndex(w2)):
                return False
        return True
        
    def getIndex(self, word):
        if word not in self.wordDict:
            self.wordDict[word] = len(self.wordDict)
        return self.wordDict[word]
```
