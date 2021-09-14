## 767. Reorganize String
### Description
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:  
Input: s = "aab"  
Output: "aba"  
Example 2:  
Input: s = "aaab"  
Output: ""  

### Solution
* HashMap + Bucket Sort
* Time Complexity: O(n)

```python
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s).most_common()
        _, max_freq = counter[0]
        if max_freq > (len(s)+1)//2:
            return ''
        
        buckets = [[] for _ in range(max_freq)]
        index = 0
        for letter, count in counter:
            for i in range(count):
                buckets[(i+index)%max_freq].append(letter)
            index += count

        return ''.join(''.join(bucket) for bucket in buckets)
```
