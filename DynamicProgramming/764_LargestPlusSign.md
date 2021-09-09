## 764. Largest Plug Sign
### Description
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

Example 1:  
1 1 1 1 1  
1 1 1 1 1  
1 ***1*** 1 1 1  
***1*** ***1*** ***1*** 1 1  
1 ***1*** 2 1 1  

Input: n = 5, mines = [[4,2]]  
Output: 2  
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.

### Solution
* Time Complexity: O(n^2)

```python
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = { tuple(mine) for mine in mines }
        dp = [[0] * n for _ in range(n)]
        res = 0
        
        for r in range(n):
            count = 0
            for c in range(n):
                count = 0 if (r, c) in banned else count+1
                dp[r][c] = count
            count = 0
            for c in range(n-1, -1, -1):
                count = 0 if (r, c) in banned else count+1
                if count < dp[r][c]:
                    dp[r][c] = count
        for c in range(n):
            count = 0
            for r in range(n):
                count = 0 if (r, c) in banned else count+1
                if count < dp[r][c]:
                    dp[r][c] = count
            count = 0
            for r in range(n-1, -1, -1):
                count = 0 if (r, c) in banned else count+1
                if count < dp[r][c]:
                    dp[r][c] = count
                if dp[r][c] > res:
                    res = dp[r][c]
        return res
```
