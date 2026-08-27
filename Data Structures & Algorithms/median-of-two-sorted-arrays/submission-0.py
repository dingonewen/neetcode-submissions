class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            # ensure the shorter one first
        
        left = 0
        right = len(nums1) - 1

        while True:
            i = (left + right) // 2   # partition index for nums1
            j = half - i - 2          # partition index for nums2

            left_1 = nums1[i] if i >= 0 else float("-inf")
            right_1 = nums1[i + 1] if (i + 1) < len(nums1) else float("inf")
            left_2 = nums2[j] if j >= 0 else float("-inf")
            right_2 = nums2[j + 1] if (j + 1) < len(nums2) else float("inf")
            
            # Check if partition is correct
            if left_1 <= right_2 and left_2 <= right_1:
                # Odd total count: median is the smallest element of the Right Half
                if total % 2 != 0:
                    return float(min(right_1, right_2))
                # Even total count: average of max of Left Half and min of Right Half
                return (max(left_1, left_2) + min(right_1, right_2)) / 2.0
            
            elif left_1 > right_2:
                right = i - 1  # Too many elements taken from nums1, search left side
            else:
                left = i + 1  # Too few elements taken from nums1, search right side