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

            if (heights[left] <= heights[right]):
                left += 1
            else:
                right -= 1
        return total_max