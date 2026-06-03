class Solution:
    def minWindow(self, s: str, t: str) -> str:  # O(26n)
        if len(s) < len(t):
            return ""
        t_count = Counter(t)
        s_count = defaultdict(int)
        left = 0
        min_length = float('inf') 
        min_left = 0
        
        for right in range(len(s)):
            s_count[s[right]] += 1
            
            while all(s_count[c] >= t_count[c] for c in t_count):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left
                
                s_count[s[left]] -= 1
                left += 1
        
        if min_length == float('inf'):
            return ""
            
        return s[min_left:min_left + min_length]