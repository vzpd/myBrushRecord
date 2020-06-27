"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        res = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                res = min(res, i - left + 1)
                sum -= nums[left]
                left += 1
            if 0 < left < len(nums):
                sum -= nums[left]
                left += 1

        if res == float('inf'):
            return 0
        return res


s = Solution()
assert s.minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) == 2
assert s.minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]) == 2
assert s.minSubArrayLen(7, [7]) == 1
assert s.minSubArrayLen(7, [3, 3, 7]) == 1
assert s.minSubArrayLen(7, [3, 3, 4]) == 2
assert s.minSubArrayLen(7, [3, 3, 0]) == 0
