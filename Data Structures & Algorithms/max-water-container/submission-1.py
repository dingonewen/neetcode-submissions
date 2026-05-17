class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        total_max = float('-inf')
        while left < right:
            width = right - left
            curr_height = min(heights[left], heights[right])
            curr_max = curr_height * width
            total_max = max(curr_max, total_max)

            if heights[left] < heights[right]:
                current_left_height = heights[left]
                left += 1
                while left < right and heights[left] <= current_left_height:
                    left += 1
            elif heights[left] > heights[right]:
                current_right_height = heights[right]
                right -= 1
                while left < right and heights[right] <= current_right_height:
                    right -= 1
            else:
                left += 1
                right -= 1
        return total_max