class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            current_char = s[right]  # char_map['a'] = 3
            
            if current_char in char_map and char_map[current_char] >= left: # teleport to the index after the same char appeared
                left = char_map[current_char] + 1
            
            current_len = right - left + 1
            max_len = max(max_len, current_len)
            char_map[current_char] = right
            
        return max_len