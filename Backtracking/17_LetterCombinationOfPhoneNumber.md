## 17. Letter Combinations of Phone Number

### Description

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

### Solution
* Backtracking
* Time Complexity: O(4^N * N)

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.digit2char = { "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        combinations = []
        self.dfs(digits, 0, [], combinations)
        
        return combinations
    
    def dfs(self, digits, index, path, combs):
        if index == len(digits):
            combs.append("".join(path))
            return
        
        letters = self.digit2char[digits[index]]
        for letter in letters:
            path.append(letter)
            self.dfs(digits, index+1, path, combs)
            path.pop()
```
