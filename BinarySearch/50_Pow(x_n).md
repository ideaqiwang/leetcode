## 50. Pow(x, n)

### Description
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:  
Input: x = 2.00000, n = 10  
Output: 1024.00000  

### Solution
* Time Complexity: O(n)
 
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        
        isPositive = (n > 0)
        if not isPositive:
            n = -n
        
        res = 1
        cur_prod = x
        while n > 0:
            if n % 2 == 1:
                res *= cur_prod
                n -= 1
            else:
                cur_prod *= cur_prod
                n //= 2
        return res if isPositive else 1/res
```
