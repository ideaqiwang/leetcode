'''
587. Two Sum - Unique Pairs

Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number.
Please return the number of pairs.

Example 1:
Input: nums = [1,1,2,45,46,46], target = 47 
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
'''

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    # Use a HashMap to store each number and its count
    # Time Complexity: O(n)
    def twoSum6(self, nums, target):
        # write your code here
        if not nums:
            return 0

        num2count = {}
        for num in nums:
            if num in num2count:
                num2count[num] += 1
            else:
                num2count[num] = 1

        pairs = set()
        for num, count in num2count.items():
            diff = target - num
            if diff in num2count and (num != diff or count > 1):
                pairs.add((num, diff) if num <= diff else (diff, num))

        return len(pairs)