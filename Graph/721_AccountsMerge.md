## 721. Accounts Merge

### Description
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:  
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]  
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]  
Explanation:  
The first and second John's are the same person as they have the common email "johnsmith@mail.com".  
The second John and Mary are different people as none of their email addresses are used by other accounts.  
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

### Solution
* Build a graph - emailA : [name, emailB]
* BFS

```python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = self.buildGraph(accounts)
        
        visited = set()
        res = []
    
        for email in graph:
            if email not in visited:
                res.append(self.bfs(graph, email, visited))
        return res
                
    def bfs(self, graph, email, visited):
        q = deque([email])
        visited.add(email)
        name = graph[email][0]
        path = []
        while q:
            node = q.popleft()
            path.append(node)
            neighbors = graph[node][1:]
            for neighbor in neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return [name] + sorted(path)

    def buildGraph(self, accounts):
        graph = {}
        
        for account in accounts:
            for i in range(1, len(account)):
                if account[i] not in graph:
                    graph[account[i]] = [account[0]]
        for account in accounts:
            for i in range(1, len(account)):
                for j in range(i+1, len(account)):
                    graph[account[i]].append(account[j])
                    graph[account[j]].append(account[i])
        return graph
```
