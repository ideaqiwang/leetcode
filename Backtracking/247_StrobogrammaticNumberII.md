## 247. Strobogrammatic Number II

### Description

Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:  
Input: n = 2  
Output: ["11","69","88","96"]  

Example 2:  
Input: n = 1  
Output: ["0","1","8"]  

### Solution
* BFS

```python
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        digits = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        q = deque()
        if n % 2 == 0:
            q.append('')
        else:
            q.append('0')
            q.append('1')
            q.append('8')
        
        res = []
        while q:
            num = q.popleft()
            if len(num) == n:
                if num[0] != '0' or n == 1:
                    res.append(num)
            else:
                for d, b in digits:
                    q.append(d + num + b)
        return res
```

* DFS

```python
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        self.digits = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        self.res = []
        if n % 2 == 0:
            self.dfs('', n)
        else:
            for c in ('0', '1', '8'):
                self.dfs(c, n)
        return self.res

    def dfs(self, path, n):
        if len(path) == n:
            if path[0] != '0' or n == 1:
                self.res.append(path)
            return
        
        for d, b in self.digits:
            self.dfs(d+path+b, n)
```
