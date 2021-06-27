'''
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

class Solution:
    '''
    1. Sort the array
    2. Fix two indices and scan with two pointers(left, right)
    Time Complexity: O(n^3)
    '''
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
    
                l, r = j+1, n-1
                while l < r:
                    sum4 = nums[i]+nums[j]+nums[l]+nums[r]
                    if sum4 == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r-1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif sum4 < target:
                        l += 1
                    else:
                        r -= 1
        return res