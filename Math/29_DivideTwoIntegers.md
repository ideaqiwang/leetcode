## 29. Divide Two Integers

### Description

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

Example 1:  
Input: dividend = 10, divisor = 3  
Output: 3  
Explanation: 10/3 = truncate(3.33333..) = 3.  

Example 2:  
Input: dividend = 7, divisor = -3  
Output: -2  
Explanation: 7/-3 = truncate(-2.33333..) = -2.  

Example 3:  
Input: dividend = -2147483648, divisor = -1  
Output: 2147483647   

### Solution

* Exponenial Search
* Time Complexity: O(n)

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        isNegtive = False
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            isNegtive = True
        
        dividend = abs(dividend)
        divisor = abs(divisor)
    
        res = 0
        shift = 31
        while shift >= 0:
            if dividend >= divisor<<shift:
                res += 1<<shift
                dividend -= divisor<<shift
            shift -= 1
        
        if isNegtive:
            res = -res
        if res < -(1<<31):
            return -(1<<31)
        if res >= (1<<31):
            return (1<<31)-1
        return res
```