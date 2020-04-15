from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 暴力解法
        # i, j = 0, 0
        # dp = []
        # while i < len(nums1) or j < len(nums2):
        #     if (i < len(nums1) and j < len(nums2)):
        #         if nums1[i] < nums2[j]:
        #             dp.append(nums1[i])
        #             i += 1
        #         else:
        #             dp.append(nums2[j])
        #             j += 1
        #     elif i < len(nums1):
        #         dp.append(nums1[i])
        #         i += 1
        #     elif j < len(nums2):
        #         dp.append(nums2[j])
        #         j += 1
        # if ((i + j) % 2 == 0):
        #     return (dp[int((i + j) / 2)] + dp[int((i + j) / 2 - 1)]) / 2
        # else:
        #     return dp[int((i + j) / 2)]
        if nums1[-1] < nums2[0]:
            pass
        elif nums1[0] > nums2[-1]:
            pass
        else:
            pass


s = Solution()

assert s.findMedianSortedArrays([], [1]) == 1
assert s.findMedianSortedArrays([1], []) == 1
assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert s.findMedianSortedArrays([1, 2], [2, 3]) == 2
assert s.findMedianSortedArrays([1, 3], [2, 4]) == 2.5
assert s.findMedianSortedArrays([2, 3], [1, 4]) == 2.5
assert s.findMedianSortedArrays([2, 3], [1, 2]) == 2
assert s.findMedianSortedArrays([3, 4], [1, 2]) == 2.5
assert s.findMedianSortedArrays([1, 2, 3], [1, 2, 3]) == 2
