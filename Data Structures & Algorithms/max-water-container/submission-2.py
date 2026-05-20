class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        total_max = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            curr_max = width * height
            total_max = max(curr_max, total_max)

            if heights[left] < heights[right]:
                left_ = heights[left]
                left += 1
                while left < right and heights[left] <= left_:
                    left += 1

            elif heights[left] > heights[right]:
                right_ = heights[right]
                right -= 1
                while left < right and heights[right] <= right_:
                    right -= 1

            else:
                left += 1
                right -= 1
                
        return total_max