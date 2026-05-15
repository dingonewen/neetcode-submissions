class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_l, prod_r = 1, 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prod_l
            prod_l *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prod_r
            prod_r *= nums[i]
        return res
        