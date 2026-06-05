class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = []
        left = 0
        right = left + k - 1
        for right in range(k - 1, len(nums)):
            left = right - k + 1
            to_add = max(nums[left:right + 1])
            res.append(to_add)
        return res