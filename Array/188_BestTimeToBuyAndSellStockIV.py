'''
188. Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices or k == 0:
            return 0
        
        transactions = []
        start = end = 0
        for i in range(1, n):
            if prices[i] >= prices[i-1]:
                end = i
            else:
                if end > start:
                    transactions.append([start, end])
                start = i
        if end > start:
            transactions.append([start, end])
        
        while len(transactions) > k:
            # check delete loss
            delete_index = 0
            min_delete_loss = sys.maxsize
            for i in range(len(transactions)):
                t = transactions[i]
                loss = prices[t[1]] - prices[t[0]]
                if loss < min_delete_loss:
                    min_delete_loss = loss
                    delete_index = i
            # check merge loss
            merge_index = 0
            min_merge_loss = sys.maxsize
            for i in range(1, len(transactions)):
                t1, t2 = transactions[i-1], transactions[i]
                loss = prices[t1[1]] - prices[t2[0]]
                if loss < min_merge_loss:
                    min_merge_loss = loss
                    merge_index = i
            # delete or merge
            if min_delete_loss < min_merge_loss:
                transactions.pop(delete_index)
            else:
                transactions[merge_index-1][1] = transactions[merge_index][1]
                transactions.pop(merge_index)
        return sum(prices[e]-prices[s] for s, e in transactions)

    '''
    Solution2: Dynamic Programming
    Keep holding the stock:
    dp[i][j][1] = dp[i-1][j][1]dp[i][j][1]=dp[i−1][j][1]

    Keep not holding the stock:
    dp[i][j][0] = dp[i-1][j][0]dp[i][j][0]=dp[i−1][j][0]

    Buying, when j>0:
    dp[i][j][1] = dp[i-1][j-1][0]-prices[i]dp[i][j][1]=dp[i−1][j−1][0]−prices[i]

    Selling:
    dp[i][j][0] = dp[i-1][j][1]+prices[i]dp[i][j][0]=dp[i−1][j][1]+prices[i]

    We can combine they together to find the maximum profit:
    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])dp[i][j][1]=max(dp[i−1][j][1],dp[i−1][j−1][0]−prices[i])
    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])dp[i][j][0]=max(dp[i−1][j][0],dp[i−1][j][1]+prices[i])
    '''
    def maxProfit2(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices or k == 0:
            return 0
        
        if 2*k > n:
            profit = 0
            for i in range(1, n):
                profit += max(0, prices[i]-prices[i-1])
            return profit
        
        # dp[i][used_k][ishold] = balance
        # ishold: 0 not hold, 1 hold
        dp = [[[-sys.maxsize]*2 for _ in range(k+1)] for _ in range(n)]
        
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        
        for i in range(1, n):
            for j in range(k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        
        profit = max(dp[n-1][j][0] for j in range(k+1))
        return profit