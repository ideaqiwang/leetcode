## Lintcode 1543. Unique Path IV

### Description

Give two integers to represent the height and width of the grid. The starting point is in the upper left corner and the ending point is in the upper right corner. You can go to the upper right corner, right or lower right corner. Find out the number of paths you can reach the end. And the result needs to mod 1000000007.

Example 1:  
Input: height = 3, width = 3  
Output: 2  

```python
class Solution:
    """
    @param height: the given height
    @param width: the given width
    @return: the number of paths you can reach the end
    """
    def uniquePath(self, height, width):
        # dp[i][j] = dp[i-1][j-1]|i>0 + dp[i][j-1] + dp[i+1][j-1]|i+1<height
        dp = [[0] * width for _ in range(height)]
        
        for j in range(width):
            for i in range(min(height, j+1)):
                if j == 1 or i == j:
                    dp[i][j] = 1
                    continue
                dp[i][j] += dp[i][j-1]

                if i > 0:
                    dp[i][j] += dp[i-1][j-1]
                if i+1<height:
                    dp[i][j] += dp[i+1][j-1]

        return dp[0][width-1] % 1000000007
```
