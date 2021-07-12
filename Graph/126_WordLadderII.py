'''
126. Word Ladder II

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
'''

class Solution:
    '''
    1. BFS traverses from end to begin to record distance.
    2. DFS traverses from start to end. Each step must ensure the distance decreased by 1.
    '''
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        wordSet.add(beginWord)
        distance = self.bfs(endWord, beginWord, wordSet)

        paths = []
        self.dfs(beginWord, endWord, [], paths, distance, wordSet)
        return paths
        
    
    def bfs(self, begin, end, wordSet):
        distance = {begin: 0}
        q = deque([begin])
        while q:
            word = q.popleft()
            for neighbor in self.getNeighbors(word, wordSet):
                if neighbor not in distance:
                    distance[neighbor] = distance[word]+1
                    q.append(neighbor)
        return distance    
    
    def dfs(self, beginWord, endWord, path, paths, distance, wordSet):
        if beginWord == endWord:
            paths.append(path+[endWord])
            return
        path.append(beginWord)
        for neighbor in self.getNeighbors(beginWord, wordSet):
            if distance[neighbor] == distance[beginWord]-1:
                self.dfs(neighbor, endWord, path, paths, distance, wordSet)
        path.pop()
            
    
    def getNeighbors(self, word, wordSet):
        words = set()
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == word[i]:
                    continue
                newWord = word[:i]+c+word[i+1:]
                if newWord in wordSet:
                    words.add(newWord)
        return words