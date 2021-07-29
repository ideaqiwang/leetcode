## 30. Substring with Concatenation of All Words

### Description

You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Example 1:  
Input: s = "barfoothefoobarman", words = ["foo","bar"]  
Output: [0,9]  
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.  
The output order does not matter, returning [9,0] is fine too.  

Example 2:  
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]  
Output: []  

Example 3:  
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]  
Output: [6,9,12]  

### Solution

* **Sliding Window**
* Time Complexity: O(n*m)
1. Use a hashmap to store each word's count.
2. Scan s starting from [0, len(words[0])). This will scan all combinations of characters.
3. Use Sliding Window technique to find matched words.

```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, total = len(s), len(words)
        word_counter = Counter(words)
        wsize = len(words[0])
        
        res = []
        for start in range(wsize):
            window_counter = defaultdict(int)
            wcount = 0
            for i in range(start, n, wsize):
                word = s[i:i+wsize]
                if word in word_counter:
                    window_counter[word] += 1
                    wcount += 1
                    while window_counter[word] > word_counter[word]:
                        p = i - wsize*(wcount-1)
                        removed_word = s[p:p+wsize]
                        window_counter[removed_word] -= 1
                        wcount -= 1
                else:
                    window_counter.clear()
                    wcount = 0
                if wcount == total:
                    res.append(i - wsize*(wcount-1))
        return res
```