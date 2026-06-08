class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        map = {')':'(', ']':'[','}':'{'}

        for c in s:
            if c in map:
                if not stack or stack.pop() != map[c]:
                    return False
                
            else:
                stack.append(c)

        return len(stack) == 0