# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        
        window_size = n - k
        min_sum = temp = sum(cardPoints[:window_size])
        
        left = 0
        for right in range(window_size, n):
            temp += cardPoints[right] - cardPoints[left]
            min_sum = min(min_sum, temp)
            left += 1  
        
        return sum(cardPoints) - min_sum
