class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        window = [0] * 26
        
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        for c in s2[:len(s1)]:
            window[ord(c) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_count[i] == window[i]:
                matches += 1
        
        if matches == 26:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            idx = ord(s2[right]) - ord('a') # add right
            window[idx] += 1 
            if window[idx] == s1_count[idx]:
                matches += 1
            elif window[idx] == s1_count[idx] + 1:
                matches -= 1

            idx = ord(s2[left]) - ord('a')  # remove left
            window[idx] -= 1
            if window[idx] == s1_count[idx]:
                matches += 1
            elif window[idx] == s1_count[idx] - 1:
                matches -= 1
            
            left += 1
            
            if matches == 26:  # ← O(1)
                return True
        
        return False