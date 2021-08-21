## 273. Integer to English Words

### Description

Convert a non-negative integer num to its English words representation.

Example 1:  
Input: num = 123  
Output: "One Hundred Twenty Three"  

Example 2:  
Input: num = 12345  
Output: "Twelve Thousand Three Hundred Forty Five"  

Example 3:  
Input: num = 1234567  
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"  

Example 4:  
Input: num = 1234567891  
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight   Hundred Ninety One"  

### Solution

* Divide numbers into a chunk of 3 digits

```python
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        self.less20 = ["", "One", "Two", "Three", "Four", "Five",
                       "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                       "Twelve", "Thirteen", "Fourteen", "Fifteen",
                       "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty",
                     "Sixty", "Seventy", "Eighty", "Ninety"]
        
        thousands = ["", "Thousand", "Million", "Billion"]
        
        res = ''
        for i in range(len(thousands)):
            if num % 1000 != 0:
                res = self.helper(num%1000) + thousands[i] + " " + res
            num //= 1000
        return res.strip()

    def helper(self, num):
        if num == 0:
            return ""
        if num < 20:
            return self.less20[num] + " "
        if num < 100:
            return self.tens[num//10] + " " + self.helper(num%10)
        return self.less20[num//100] + " Hundred " + self.helper(num%100)
```
