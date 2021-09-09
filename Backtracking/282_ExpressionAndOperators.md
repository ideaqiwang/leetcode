## 282. Expression Add Operators
### Description
Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

Example 1:  
Input: num = "123", target = 6  
Output: ["1*2*3","1+2+3"]  

Example 2:  
Input: num = "105", target = 5  
Output: ["1*0+5","10-5"]  

### Solution
* Backtracking

```python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.res = []
        self.dfs(num, 0, '', 0, 0, target)
        return self.res
    
    def dfs(self, numStr, idx, expr, prev, curr, target):
        if idx == len(numStr):
            if curr == target:
                self.res.append(expr)
            return
        
        for i in range(idx, len(numStr)):
            operandStr = numStr[idx: i+1]
            num = int(operandStr)
            if idx == 0:
                self.dfs(numStr, i+1, operandStr, num, num, target)
            else:
                self.dfs(numStr, i+1, expr+'+'+operandStr, num, curr+num, target)
                self.dfs(numStr, i+1, expr+'-'+operandStr, -num, curr-num, target)
                self.dfs(numStr, i+1, expr+'*'+operandStr, prev*num, curr-prev+prev*num, target)
            
            # Skip invalid numbers starting with 0 such as 01, 02...
            if num == 0:
                break
```
