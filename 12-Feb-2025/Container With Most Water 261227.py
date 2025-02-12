# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the current area
            area = min(height[left], height[right]) * (right - left)
            # Update the maximum area
            max_area = max(max_area, area)
            
            # Move the pointer corresponding to the smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area