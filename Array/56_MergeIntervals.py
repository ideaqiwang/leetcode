'''
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

class Solution:
    '''
    1. Sort intervals with the lower bound of each interval.
    2. Compare the upper bound to decide if need to merge.
    A. Don't merge:
    |____|
           |____| 
    B. Merge
    1. |____|
            |____|
    2. |____|
          |____|
    3. |_____|
        |___|
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        
        merged = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            if merged[-1][1] >= sorted_intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], sorted_intervals[i][1])
            else:
                merged.append(sorted_intervals[i])
        return merged