## 809. Expressive Words
### Description

Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.

Example 1:  
Input: s = "heeellooo", words = ["hello", "hi", "helo"]  
Output: 1  
Explanation:   
We can extend "e" and "o" in the word "hello" to get "heeellooo".  
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.  
Example 2:  
Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]  
Output: 3  

### Solution
* Generate a list of char and its frequence given a word. Then compare them.

```python
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        template = self.getSignature(s)
        
        count = 0
        for i in range(len(words)):
            if self.isStretchy(words[i], template):
                count += 1
        return count
    
    def isStretchy(self, word, template):
        signature = self.getSignature(word)
        if len(signature) != len(template):
            return False

        for i in range(len(signature)):
            if signature[i][0] != template[i][0]:
                return False
            if signature[i][1] > template[i][1]:
                return False
            if signature[i][1] < template[i][1] and template[i][1] < 3:
                return False
        return True
    
    def getSignature(self, word):
        if not word:
            return []
        signature = []
        char = word[0]
        count = 0
        for c in word:
            if c == char:
                count += 1
            else:
                signature.append((char, count))
                char = c
                count = 1
        signature.append((char, count))
        return signature
```
