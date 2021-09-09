## 848. Shifting Letters
### Description
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.  
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

Example 1:  
Input: s = "abc", shifts = [3,5,9]  
Output: "rpl"  
Explanation: We start with "abc".  
After shifting the first 1 letters of s by 3, we have "dbc".  
After shifting the first 2 letters of s by 5, we have "igc".  
After shifting the first 3 letters of s by 9, we have "rpl", the answer.  
Example 2:  
Input: s = "aaa", shifts = [1,2,3]  
Output: "gfd"  

### Solution
* Prefix Sum

```python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        def shift(c, step):
            idx = ord(c) - ord('a')
            return chr(ord('a')+(idx+step)%26)
    
        n = len(s)
        final_shifts = list(shifts)
        for i in range(n-2, -1, -1):
            final_shifts[i] += final_shifts[i+1]

        charList = []
        for i, c in enumerate(s):
            charList.append(shift(c, final_shifts[i]))
        return ''.join(charList)
```
