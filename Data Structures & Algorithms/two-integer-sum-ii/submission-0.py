class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                res.append(left + 1)
                res.append(right + 1)
                return res
            elif sum < target:
                left += 1
            else:
                right -= 1
        return []