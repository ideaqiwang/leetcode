'''
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 
Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
'''

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxVals = [] # min heap
        self.minVals = [] # max heap
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minVals, -num)
        heapq.heappush(self.maxVals, -heapq.heappop(self.minVals))
        
        if len(self.minVals) < len(self.maxVals):
            heapq.heappush(self.minVals, -heapq.heappop(self.maxVals))
        
    def findMedian(self) -> float:
        return -self.minVals[0] if len(self.minVals) > len(self.maxVals) else (-self.minVals[0]+self.maxVals[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()