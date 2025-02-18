# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n = len(tasks)
        k = len(processorTime)
        size = n // k
        remainder = n % k
        parts = []
        start = 0
        tasks.sort()
        processorTime.sort()
        for i in range(k):
            extra = 1 if i < remainder else 0  # Distribute extra elements
            end = start + size + extra
            parts.append(tasks[start:end])
            start = end
        max_ele = []
        for i in parts:
            max_ele.append(max(i))
        
        print(processorTime, max_ele)
        ans = 0
        for i in range(k):
            # print(processorTime[i] + max_ele[k-1-i])
            ans = max(processorTime[i] + max_ele[k-1-i], ans)
            
        return ans

