class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        nums.sort();
        for left in range (0, len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:   # skip duplicate element
                continue
            mid = left + 1
            right = len(nums) - 1
            while (mid < right):
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum == 0:
                    res.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                    # skip duplicate values
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < 0:
                    mid += 1
                else:
                    right -= 1
        return res
            

        