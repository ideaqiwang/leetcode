'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
'''

class Solution:
    def twoSum(self, nums, i, res):
        seen = set()
        j = i+1
        n = len(nums)
        while j < n:
            complement = -nums[i]-nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j+1 < n and nums[j] == nums[j+1]:
                    j += 1
            seen.add(nums[j])
            j += 1
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

# Use 3 pointers
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.findTriplets(nums, i, res)
        return res
    
    def findTriplets(self, nums, idx, res):
        l = idx + 1
        r = len(nums) - 1
        while l < r:
            total = nums[idx] + nums[l] + nums[r]
            if total == 0:
                res.append([nums[idx], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif total < 0:
                l += 1
            else:
                r -= 1