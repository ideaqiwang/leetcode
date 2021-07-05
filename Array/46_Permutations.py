'''
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        self.dfs(nums, visited, [], res)
        return res
        
    def dfs(self, nums, visited, permutation, res):
        if len(permutation) == len(nums):
            res.append(list(permutation))
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, permutation, res)
            permutation.pop()
            visited[i] = False