## 43. Multiply Strings

### Description
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:  
Input: num1 = "2", num2 = "3"  
Output: "6"  

Example 2:  
Input: num1 = "123", num2 = "456"  
Output: "56088"  

### Solution

The length of product would not be longer than len(num1)+len(num2).

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
    
        def toNum(c):
            return ord(c) - ord('0')
        
        def toStr(digit):
            return chr(digit+ord('0'))
        
        n = len(num1) + len(num2)
        product = [0] * n
        
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                product[i+j+1] += toNum(num1[i]) * toNum(num2[j])

        for i in range(n-1, 0, -1):
            product[i-1] += product[i] // 10
            product[i] %= 10 
 
        res = ''
        for i in range(n):
            if product[i] == 0 and not res:
                continue
            res += toStr(product[i])
        return res
```