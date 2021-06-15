'''
269. Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.
A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ''
        if len(words) == 1:
            return words[0]
        
        graph = self.buildGraph(words)
        if not graph:
            return ''
        
        indegree = { node: 0 for node in graph }
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        startChars = [ c for c in indegree if indegree[c] == 0 ]
        q = deque(startChars)
        order = ''

        while q:
            c = q.popleft()
            order += c
            for nextChar in graph[c]:
                indegree[nextChar] -= 1
                if indegree[nextChar] == 0:
                    q.append(nextChar)
            
        return order if len(order) == len(indegree) else ''
        
    def buildGraph(self, words):
        graph = {} # a : {b, c} => a comes before b and c
        for w in words:
            for c in w:
                if c not in graph:
                    graph[c] = set()
    
        for i in range(len(words)-1):
            minLen = min(len(words[i]), len(words[i+1]))
            for j in range(minLen):
                c1, c2 = words[i][j], words[i+1][j]
                if c1 != c2:
                        graph[c1].add(c2)
                        break
                if j == minLen-1 and len(words[i]) > len(words[i+1]):
                    return None
        return graph