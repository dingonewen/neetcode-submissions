class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)
        longest_streak = 0
        for n in set_:
            if (n - 1) not in set_:
                curr_num = n
                curr_streak = 1
                while (curr_num + 1) in set_:
                    curr_num += 1
                    curr_streak += 1
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak
        