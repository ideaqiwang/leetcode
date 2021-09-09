## 20. Valid Parentheses
### Description
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example 1:  
Input: s = "()[]{}"  
Output: true  

Example 2:  
Input: s = "(]"  
Output: false  

Example 3:  
Input: s = "([)]"  
Output: false  

### Solution
* Use a stack to store open brackets

```python
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 == 1:
            return False
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in mapping:
                if not stack or mapping[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack
```
