# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        if n == 1:
            return self.nums[0]
        if n%2 == 1:
            idx = n//2
            return self.nums[idx]
        else:
            idx_left = (n//2) - 1
            idx_right = idx_left + 1
            ans = (self.nums[idx_left] + self.nums[idx_right])/2
            return ans



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()