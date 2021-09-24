## 22. Generate Parentheses
### Description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:  
Input: n = 3  
Output: ["((()))","(()())","(())()","()(())","()()()"]  

Example 2:  
Input: n = 1  
Output: ["()"]  

### Solution
* Backtracking

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.dfs(n, n, [])
        return self.res
    
    def dfs(self, left, right, path):
        if right == 0:
            self.res.append(''.join(path))
            return
        
        if left > 0:
            path.append('(')
            self.dfs(left-1, right, path)
            path.pop()
        if right > left:
            path.append(')')
            self.dfs(left, right-1, path)
            path.pop()
```
