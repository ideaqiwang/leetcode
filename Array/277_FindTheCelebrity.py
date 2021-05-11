'''
277. Find the Celebrity

Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Example 1:
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:
Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.
'''

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    '''
    1. Use an cache to minimize the API calls of knows()
    2. Filter out possibile candidates
       Given the fact that if A knows B, A CANNOT be a celebrity. B is an candidate.
       A. Firstly, the candidate is 0
       B. Check if candidate knows $i:
          Yes: update $candidate to $i
          No: increment $i by one
       C. In the end, we only have one candidate.
    3. Check if $candidate is a celebrity
    '''
    def __init__(self):
        self.cache = {} # (a, b) -> whether a knows b

    def cacheKnows(self, a, b):
        key = (a, b)
        if key not in self.cache:
            self.cache[key] = knows(a, b)
        return self.cache[key]

    def isCelebrity(self, index, n):
        for i in range(n):
            if i == index:
                continue
            if self.cacheKnows(index, i) or not self.cacheknows(i, index):
                return False
        return True

    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(n):
            if self.cacheKnows(candidate, i):
                candidate = i
        if self.isCelebrity(candidate, n):
            return candidate
        return -1