## 67. Add Binary

### Description

Given two binary strings a and b, return their sum as a binary string.

Example 1:  
Input: a = "11", b = "1"  
Output: "100"  

Example 2:  
Input: a = "1010", b = "1011"  
Output: "10101"  

### Solution
* Solution 1: Simulation
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        i, j = m-1, n-1
        carry = 0
        buf = []
        while i >= 0 or j >= 0:
            if i >= 0 and a[i] == '1':
                carry += 1
            if j >= 0 and b[j] == '1':
                carry += 1
    
            buf.append(str(carry%2))
            carry //= 2
    
            i -= 1
            j -= 1
        
        if carry == 1:
            buf.append('1')

        return ''.join(buf[::-1])
```

* Solution 2: Bit Manipulation
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]
```
