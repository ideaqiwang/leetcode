'''
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
'''

class Solution:
# Solution 1:
# Suppose there're n elements in the array. We have to change n times in total.
# We start with start index 0, save a copy to $cur. Use $prev to store the original element.
# Then calculate $nextIndex = ($cur + k) % n
# Save nums[nextIndex] to $temp
# Update nums[nextIndex] = $prev
# Update $prev = $temp and increment $count
# We keep doing this until $cur == $start
# Increment $start and start the next iteration.
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 1:
            return
        k %= length
        
        start = count = 0
        while count < length:
            current, prev = start, nums[start]
            while True:
                nxtIdx = (current+k) % length
                nums[nxtIdx], prev = prev, nums[nxtIdx]
                current = nxtIdx
                count += 1
                if start == current:
                    break
            start += 1

# Solution 2:
# 1. Reverse the whole array
# 2. Reverse the first k elemets
# 3. Reverse the rest elements
    def reverse(self, nums, start, end):
        l, r = start, end
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate2(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 1:
            return
        k %= length
        
        self.reverse(nums, 0, length-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, length-1)