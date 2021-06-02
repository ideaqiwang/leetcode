'''
259. 3Sum Smaller

Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example 1:
Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

Example 2:
Input: nums = [], target = 0
Output: 0

Example 3:
Input: nums = [0], target = 0
Output: 0
'''

class Solution:
    def twoSumSmaller(self, nums, start, target):
        l, r = start, len(nums)-1
        total = 0
        while l < r:
            if nums[l]+nums[r] < target:
                total += r - l
                l += 1
            else:
                r -= 1
        return total

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = 0
        for i in range(len(nums)-2):
            total += self.twoSumSmaller(nums, i+1, target-nums[i])
        return total