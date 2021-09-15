'''
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

class Solution:
    '''
    Quick Select Algorithm
    Time Complexity: Average - O(n), Worst - O(n^2)
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums)-1, k-1)

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        l, r = start, end
        pivot = nums[(l+r)//2]
        while l <= r:
            while l <= r and nums[l] > pivot:
                l += 1
            while l <= r and nums[r] < pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        if start <= r and r >= k:
            return self.quickSelect(nums, start, r, k)
        if l <= end and l <= k:
            return self.quickSelect(nums, l, end, k)
        return nums[k]

class Solution2:
    '''
    Use Min-Heap to store each number.
    Pop the top value when the length is greater than k.
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        
        for num in nums:
            heapq.heappush(hp, num)
            if len(hp) > k:
                heapq.heappop(hp)
        return heapq.heappop(hp)