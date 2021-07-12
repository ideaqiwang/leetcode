'''
128. Longest Concecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 1
        numSet = set(nums)
        
        for num in nums:
            if num not in numSet:
                continue
            curLength = 1
            numSet.discard(num)
            l, r = num-1, num+1
            while l in numSet:
                numSet.discard(l)
                l -= 1
                curLength += 1
            while r in numSet:
                numSet.discard(r)
                r += 1
                curLength += 1
            longest = max(longest, curLength)
        return longest