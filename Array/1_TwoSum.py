'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

------------------------------------------------------------------------------

Solution:
1. Create a dictionary $num2index to store each number and its index to a Dictionary
2. Iterate each number $num in the list
3. Calculator the difference $diff of target and the number
4. Check if $diff is in the dictionary
   Yes: return the current index and the index of $diff
   No: save the $num and its index to $num2index.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2index = {}

        for i in range(len(nums)):
            n= nums[i]
            diff = target - n
            if diff in num2index:
                return [i, num2index[diff]]
            num2index[n] = i

