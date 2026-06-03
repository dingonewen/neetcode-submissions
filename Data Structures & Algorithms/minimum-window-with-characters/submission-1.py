class Solution:
    def minWindow(self, s: str, t: str) -> str:  # O(n)
        if len(s) < len(t):
            return ""
        t_count = Counter(t)
        window = defaultdict(int)
        
        have = 0
        need = len(t_count)
        
        left = 0
        res_left = 0
        res_len = float('inf')
        
        for right in range(len(s)):
            char = s[right]
            window[char] += 1
            
            if char in t_count and window[char] == t_count[char]:
                have += 1
            
            while have == need:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res_left = left
                
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        
        if res_len == float('inf'):
            return ""
        return s[res_left:res_left + res_len]