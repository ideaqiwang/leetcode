## 7. Reverse Integer
### Description
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:  
Input: x = 123  
Output: 321  
Example 2:  
Input: x = -123  
Output: -321  
Example 3:  
Input: x = 120  
Output: 21  

### Solution
* Time Complexity: O(n)

```python
class Solution:
    def reverse(self, x: int) -> int:
        INTMAX, INTMIN = (1<<31)-1, -(1<<31)

        sign = 1
        if x < 0:
            sign, x = -1, -x
        res = 0
        while x != 0:
            num = x % 10
            x = x // 10
            if res > INTMAX/10 or (res == INTMAX/10 and num > 7):
                return 0
        
            res = res*10 + num
        return res * sign
```
