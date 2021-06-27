'''
16. 3 Sum Closest

Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1

Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    '''
    1. Sort the array
    2. Use two pointers(left, right) to scan
    Time Complexity: O(n^2)
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = sys.maxsize
        sum3 = None
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                tempSum3 = nums[i]+nums[l]+nums[r]
                tempDiff = abs(tempSum3 - target)
                if tempDiff < diff:
                    diff = tempDiff
                    sum3 = tempSum3
                if tempSum3 < target:
                    l += 1
                else:
                    r -= 1
        return sum3