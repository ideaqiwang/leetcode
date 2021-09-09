## 68. Text Justification
### Description

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:  
A word is defined as a character sequence consisting of non-space characters only.  
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.  
The input array words contains at least one word.  
 

Example 1:  
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16  
Output:  
[  
   "This    is    an",  
   "example  of text",  
   "justification.  "  
]  

### Solution
* Simulation

```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i, n = 0, len(words)
        while i < n:
            line_words = []
            j = i
            curLen = 0
            while j < n and curLen+1+len(words[j]) <= maxWidth+1:
                curLen = curLen + 1 + len(words[j])
                j += 1
            end = j if j == i else j-1
            if j < n:
                res.append(self.formatLine(i, end, curLen-1, words, maxWidth))
            else:
                res.append(self.formatLastLine(i, end, words, maxWidth))
            i = j
        return res

    def formatLine(self, start, end, length, words, maxWidth):
        n = end - start + 1
        if n == 1:
            return words[start] + ' ' * (maxWidth-len(words[start]))
        
        gap_count = n-1
        min_space_count = (maxWidth-length)//gap_count + 1
        spaces = [min_space_count] * gap_count
        extraSpaces = (maxWidth-length) % gap_count
        for i in range(extraSpaces):
            spaces[i] += 1
        
        line = words[start]
        for i in range(1, n):
            line += ' '*spaces[i-1] + words[start+i]
        return line
    
    def formatLastLine(self, start, end, words, maxWidth):
        line = words[start]
        for i in range(start+1, end+1):
            line += ' ' + words[i]
        return line + ' '*(maxWidth-len(line))
```
