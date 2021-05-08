'''
27. Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Note: The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.
'''

class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        '''
        First of all, use two points $left, $right which points to the beginnning and the end.
        As long as $left <= $right, we keeping doing the followings.
        If the left num equals the target $val, copy the right num to the left num and decrease $right by one.
        Otherwise, increase $left by one.
        In the end, return $left.
        '''
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left

    def removeElement2(self, nums: List[int], val: int) -> int:
        '''
        Consider the elements to be removed as non-existent.
        In a single pass, we keep copying the visible elements in-place.
        Use two pointers $slow and $fast to iterate the list $nums.
        $slow points to the length of new array. $fast points to each number.
        As long as nums[fast] NOT equals the target, we copy nums[fast] to nums[slow] and
        increase $slow by one.
        '''
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow