"""
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Approach: Two Pointers (Converging)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            width = right - left
            area = width * min(height[left], height[right])
            result = max(result, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result