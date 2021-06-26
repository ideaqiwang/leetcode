'''
912. Sort a Array

Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
'''

class Solution:
    # Quicksort with Hoare partition scheme
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums
  
    def quickSort(self, nums, left, right):
        if left >= right:
            return

        pivot = self.partition(nums, left, right)
        self.quickSort(nums, left, pivot)
        self.quickSort(nums, pivot+1, right)
        
        
    def partition(self, nums, left, right):
        pivot = nums[(left+right)//2]
        
        i, j = left, right
        while True:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
        
            if i >= j:
                return j
            
            nums[i], nums[j] = nums[j], nums[i]
    
            i += 1
            j -= 1
