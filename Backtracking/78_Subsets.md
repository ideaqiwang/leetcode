## 78. Subsets

### Description

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:  
Input: nums = [1,2,3]  
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]  

### Solution
* Bracktracking
* Time Complexity: O(n)

```
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, 0, [])
        return self.res
        
    def dfs(self, nums, idx, path):
        self.res.append(list(path))
  
        for i in range(idx, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i+1, path)
            path.pop()
```
