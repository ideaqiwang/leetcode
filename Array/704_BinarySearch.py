'''
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums)-1
        '''
        Here, we use start+1 < end to prevent dead loop
        when find the last position of a target.
        '''
        while start+1 < end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        
        '''
        When exit the while loop, start and end are next to each other.
        We need to check them again.
        '''
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1