class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        char_map = {}

        dp[0] = 1
        char_map[s[0]] = 0
        max_ans = 1
        
        for i in range(1, n):
            current_char = s[i]
            last_seen = char_map.get(current_char, -1)
            
            dp[i] = min(dp[i-1] + 1, i - last_seen)
            
            char_map[current_char] = i
            max_ans = max(max_ans, dp[i])
            
        return max_ans