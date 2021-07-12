'''
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

class Solution1:
    # Min Heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2count = defaultdict(int)
        for num in nums:
            num2count[num] += 1
        
        hq = []
        for num, count in num2count.items():
            heapq.heappush(hq, (count, num))
            if len(hq) > k:
                heapq.heappop(hq)
        return [item[1] for item in hq]

class Solution2:
    # Quick Select
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2count = defaultdict(int)
        for num in nums:
            num2count[num] += 1
        vals = [ key for key in num2count.keys()]

        self.quickSelect(vals, num2count, 0, len(vals)-1, k)

        return vals[:k]
    
    def quickSelect(self, nums, num2count, start, end, k):
        if start == end:
            return
        
        l, r = start, end
        pivot = num2count[nums[(l+r)//2]]
        while l <= r:
            while l<=r and num2count[nums[l]] > pivot:
                l += 1
            while l<=r and num2count[nums[r]] < pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if start<=r and r >= k:
            self.quickSelect(nums, num2count, start, r, k)
        if r<=end and l <= k:
            self.quickSelect(nums, num2count, l, end, k)