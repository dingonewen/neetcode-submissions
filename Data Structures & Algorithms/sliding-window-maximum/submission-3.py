class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: # O(n)
        if not nums:
            return []
        res = []
        dq = deque()  # dq save the indices of the max element, monotonic decrease
        
        for i in range(len(nums)):
            if dq and dq[0] < i - k + 1:  # remove the index out of k
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[i]: # remove the elements less than the current element
                dq.pop()
            
            dq.append(i)  # add the current element
            
            if i >= k - 1:  # record the result
                res.append(nums[dq[0]])  
        
        return res