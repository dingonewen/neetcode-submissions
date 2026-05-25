class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1
            
            current_len = right - left + 1
            max_len = max(max_len, current_len)
            char_map[current_char] = right
            
        return max_len