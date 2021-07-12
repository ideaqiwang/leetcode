'''
264. Ugly Number II

Given an integer n, return the nth ugly number.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
'''

class Solution1:
    # Min Heap
    def nthUglyNumber(self, n: int) -> int:
        minHeap = []
        seen = set([1])
        heapq.heappush(minHeap, 1)
        
        factors = (2, 3, 5)
        curUgly = 1
        for _ in range(n):
            curUgly = heapq.heappop(minHeap)
            for factor in factors:
                newUgly = curUgly*factor
                if newUgly not in seen:
                    heapq.heappush(minHeap, newUgly)
                    seen.add(newUgly)
        return curUgly

class Solution2:
    '''
    Dynamic Programming
    dp[i] = min(dp[l2]*2, dp[l3]*3, dp[l5]*5)
    '''
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        l2 = l3 = l5 = 0
        for i in range(1, n):
            newUgly2, newUgly3, newUgly5 = dp[l2]*2, dp[l3]*3, dp[l5]*5
            dp[i] = min([newUgly2, newUgly3, newUgly5])
            # Three if statements rather than elif
            # It'd filter out duplicates.
            if dp[i] == newUgly2:
                l2 += 1
            if dp[i] == newUgly3:
                l3 += 1
            if dp[i] == newUgly5:
                l5 += 1
        return dp[n-1]