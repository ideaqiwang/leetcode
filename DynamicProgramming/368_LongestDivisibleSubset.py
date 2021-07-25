'''
368. Longest Divisible Subset

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
'''

class Solution:
    '''
    1. First sort the array
    2. dp[num] refers to the length of the divisible subset whose largest element is num.
    Time Complexity: O(nlogn + n*sqrt(n) + sqrt(n))
    '''
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp, prev = {}, {}
        for num in nums:
            dp[num] = 1
            prev[num] = -1

        lastNum = nums[0]
        for num in nums:
            for factor in self.getFactors(num):
                if factor not in dp:
                    continue

                if dp[factor]+1 > dp[num]:
                    dp[num] = dp[factor] + 1
                    prev[num] = factor
                    if dp[num] > dp[lastNum]:
                        lastNum = num
        
        res = []
        while lastNum != -1:
            res.append(lastNum)
            lastNum = prev[lastNum]
        return res
    
    def getFactors(self, num):
        if num == 1:
            return []
        
        factor = 1
        factors = []
        sqrtRoot = sqrt(num)
        while factor <= sqrtRoot:
            if num % factor == 0:
                factors.append(factor)
                if factor != sqrtRoot and factor != 1:
                    factors.append(num//factor)
            factor += 1
        return factors
