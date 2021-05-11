'''
997. Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
'''

class Solution:
    # If a trust b, a can NOT be the judge
    # Build a degree array which equals indegree - outdegree
    # If a trusts b, degree[a]-- and degree[b]++
    # Iterate throught 1 to N, find which degree is N-1
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N-1:
            return -1
        degree = [0] * (N+1) # indegree - outdegree
        for a, b in trust: # a -> b
            degree[b] += 1
            degree[a] -= 1
        for i in range(1, N+1):
            if degree[i] == N-1:
                return i
        return -1