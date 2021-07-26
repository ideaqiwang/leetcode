## 1423. Maximum Points You Can Obtain from Cards

### Description
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:  
Input: cardPoints = [1,2,3,4,5,6,1], k = 3  
Output: 12  
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.  

Example 2:  
Input: cardPoints = [2,2,2], k = 2  
Output: 4  
Explanation: Regardless of which two cards you take, your score will always be 4.  

Example 3:  
Input: cardPoints = [9,7,7,9,7,7,9], k = 7  
Output: 55  
Explanation: You have to take all the cards. Your score is the sum of points of all cards.  

### Solution
#### Solution 1 - Sliding Window
1. Calculate the total sum of all elements.
2. Find the minimum sum of window with length n-k
```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalSum = sum(cardPoints)
        n = len(cardPoints)
        if n <= k:
            return totalSum

        w = n - k
        l = 0
        windowSum = 0
        minWindowSum = sys.maxsize
        
        for r in range(n):
            windowSum += cardPoints[r]
            if r-l+1 == w+1:
                windowSum -= cardPoints[l]
                l += 1
            if r >= w-1:
                minWindowSum = min(minWindowSum, windowSum)
        return totalSum - minWindowSum
```

#### Solution 2 - Dynamic Programming

1. frontWindow refers to the prefix sum and backWindow referes to the suffix sum.
2. When choose i element(s) from front, must choose k-i element(s) from back.

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n <= k:
            return sum(cardPoints)

        frontWindow = [0] * (k+1)
        backWindow = [0] * (k+1)
        
        for i in range(k):
            frontWindow[i+1] = frontWindow[i] + cardPoints[i]
            backWindow[i+1] = backWindow[i] + cardPoints[n-i-1]
        score = 0
        for i in range(k+1):
            score = max(score, frontWindow[i]+backWindow[k-i])
        return score
```