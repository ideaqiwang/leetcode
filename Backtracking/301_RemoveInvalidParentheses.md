## 301. Remove Invalid Parentheses

### Description

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Example 1:  
Input: s = "()())()"  
Output: ["(())()","()()()"]  

Example 2:  
Input: s = "(a)())()"  
Output: ["(a())()","(a)()()"]  

Example 3:  
Input: s = ")("  
Output: [""] 

### Solution

```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]

        q = deque([s])
        visited = set([s])
    
        res = []
        found = False
        while q:
            entry = q.popleft()
            if self.isValid(entry):
                found = True
                res.append(entry)
            elif not found:
                for i in range(len(entry)):
                    if entry[i] == '(' or entry[i] == ')':
                        new_str = entry[:i] + entry[i+1:]
                        if new_str not in visited:
                            q.append(new_str)
                            visited.add(new_str)
        return res
                
    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                if count < 1:
                    return False
                count -= 1
        return count == 0
```
