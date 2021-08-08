## 47. Permutations II

### Description

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:  
Input: nums = [1,1,2]  
Output:  
[[1,1,2],  
 [1,2,1],  
 [2,1,1]]  

### Solution
* Create a hash map num2count to group the same numbers together
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [], Counter(nums))
        return self.res
    
    def dfs(self, nums, path, num2count):
        if len(path) == len(nums):
            self.res.append(list(path))
            return
        
        for num in num2count.keys():
            if num2count[num] > 0:
                path.append(num)
                num2count[num] -= 1
                self.dfs(nums, path, num2count)
                path.pop()
                num2count[num] += 1
```