class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            # Calculate the current area
            current_water = min(heights[l], heights[r]) * (r - l)
            max_water = max(max_water, current_water)
            
            # Move the pointer pointing to the shorter bar
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return max_water