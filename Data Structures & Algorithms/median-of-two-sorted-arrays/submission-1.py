class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # Ensure A is the shorter array
        if len(A) > len(B):
            A, B = B, A

        left, right = 0, len(A) - 1

        while True:
            # Handle empty array case safely
            i = (left + right) // 2 if right >= 0 else -1
            j = half - i - 2

            left_1 = A[i] if i >= 0 else float("-inf")
            right_1 = A[i + 1] if (i + 1) < len(A) else float("inf")
            left_2 = B[j] if j >= 0 else float("-inf")
            right_2 = B[j + 1] if (j + 1) < len(B) else float("inf")

            # Correct partition found
            if left_1 <= right_2 and left_2 <= right_1:
                if total % 2 != 0:
                    return float(min(right_1, right_2))
                return (max(left_1, left_2) + min(right_1, right_2)) / 2.0

            # Too many elements taken from A
            elif left_1 > right_2:
                right = i - 1
            # Too few elements taken from A
            else:
                left = i + 1