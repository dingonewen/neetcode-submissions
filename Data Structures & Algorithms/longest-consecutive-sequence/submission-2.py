class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_set = set(nums)
        longest_streak = 0
        for num in curr_set:
            if (num - 1) not in curr_set:
                curr_num = num
                curr_streak = 1
                while (curr_num + 1) in curr_set:
                    curr_num += 1
                    curr_streak += 1
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak