'''
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Follow-up: Could you solve the problem in linear time and in O(1) space?

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]
'''

class Solution:
    '''
    Boyer-Moore Voting Algorithm
    There can be at most one majority element which is more than ⌊n/2⌋ times.
    There can be at most two majority elements which are more than ⌊n/3⌋ times.
    There can be at most three majority elements which are more than ⌊n/4⌋ times.
    '''
    def majorityElement(self, nums):
        if not nums:
            return []

        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        # Verify candidates meet requirements
        thredhold = len(nums) // 3
        res = []
        for c in (candidate1, candidate2):
            if nums.count(c) > thredhold:
                res.append(c)
        return res