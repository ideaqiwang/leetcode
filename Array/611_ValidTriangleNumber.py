'''
611. Valid Triangle Number

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:
Input: nums = [4,2,3,4]
Output: 4
'''

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for longest in range(n-1, 1, -1):
            l, r = 0, longest-1
            while l < r:
                if nums[l]+nums[r] > nums[longest]:
                    count += r-l
                    r -= 1
                else:
                    l += 1
        return count