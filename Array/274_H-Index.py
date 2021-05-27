'''
274. H-Index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.
According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.
If there are several possible values for h, the maximum one is taken as the h-index.

Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1
'''

class Solution:
    '''
    H-Index's range is [0, n] given a citations which length is n.
    Sort the array by couting sort.
    Find the maximum square in the histgram.
                   | |
              | |  | |
         | |  | |  | |
         | |  | |  | | h = 3
    | |  | |  | |  | | 
     0    1    2    3
             h = 3
    '''
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n = len(citations)
        papers = [0] * (n+1)
        for c in citations:
            papers[min(n, c)] += 1
        h = n
        s = papers[n]
        while h > s:
                h -= 1
                s += papers[h]
        return h