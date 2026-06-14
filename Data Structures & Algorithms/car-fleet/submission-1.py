class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0
        cars = sorted(zip(position, speed), reverse=True) # bundle (position, speed) from large to small
        stack = [] 
        
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)   # push means new fleet (cannot catch the front car)
        
        return len(stack)