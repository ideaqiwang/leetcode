'''
80. Remove Duplicates from Sorted Array II
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
Explanation: Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3]
Explanation: Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively. It doesn't matter what values are set beyond the returned length.
'''

class Solution:
    '''
    1. Define two pointers $slow and $fast. $fast iterates each number. $slow keeps track where we can overwrite an element.
    2. Define $duplicates keeps track of the count of a particular element in the array.
    3. Start with index 1
    4. If we find the current element is the same as the previous one i.e. nums[fast] == nums[fast-1], we increment $duplicates.
       A. If $duplicates > 2, we have encountered an unwanted duplicate number. In such case, we simplely move forward i.e. increment $fast but not $slow.
       B. However, if $duplicates <= 2, we can move the number by $nums[slow] = $nums[fast]. And increment $slow by one.
    5. if the the current element is NOT the same as the previous one. We simplely reset $duplicates to 1.
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums):
        if length <= 2:
            return length
        
        slow = 1
        duplicates = 1
        for fast in range(1, length):
            if nums[fast] == nums[fast-1]:
                duplicates += 1
            else:
                duplicate = 1
            if duplicates <= 2:
                nums[slow] = nums[fast]
                slow += 1
        return slow
