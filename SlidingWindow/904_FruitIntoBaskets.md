## 904. Fruit Into Baskets

### Description
ou are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

* You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.  
* Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.  
* Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:  
Input: fruits = [1,2,1]  
Output: 3  
Explanation: We can pick from all 3 trees.  

Example 2:  
Input: fruits = [0,1,2,2]  
Output: 3  
Explanation: We can pick from trees [1,2,2].  
If we had started at the first tree, we would only pick from trees [0,1].  

Example 3:  
Input: fruits = [1,2,3,2,2]  
Output: 4  
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].  

Example 4:  
Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]  
Output: 5  
Explanation: We can pick from trees [1,2,1,1,2].  

### Solution
**Sliding Window** algorithm
1. Initialize L, R to 0.
2. Outer loop to move R to right and update typy2count.
3. If type2count has more than 2 keys, it breaks the constraint. Move L to right and update type2count.
4. Update the optimized value.

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        type2count = defaultdict(int)
        
        count = 0
        l = 0
        
        for r in range(n):
            type2count[fruits[r]] += 1
            while l < n and len(type2count) > 2:
                type2count[fruits[l]] -= 1
                if type2count[fruits[l]] == 0:
                    del type2count[fruits[l]]
                l += 1
            count = max(count, r-l+1)
        return count
```