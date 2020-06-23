"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
"""
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def findDuplicate(self, nums: List[int]) -> int:
        # l, r = 1, len(nums) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     count = 0
        #     for x in nums:
        #         count += 1 if x < mid else 0
        #     if count > mid - 1:
        #         r = mid - 1
        #     elif count <= mid - 1:
        #         l = mid + 1
        #
        # return l - 1
        # 快慢指针
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        start = 0
        while start != slow:
            start = nums[start]
            slow = nums[slow]

        return start


s = Solution()
assert s.findDuplicate([1, 1, 3, 4, 2]) == 1
assert s.findDuplicate([1, 1]) == 1
assert s.findDuplicate([1, 2, 2]) == 2
assert s.findDuplicate([1, 1, 2]) == 1
assert s.findDuplicate([1, 3, 4, 2, 2]) == 2
assert s.findDuplicate([3, 1, 3, 4, 2]) == 3
assert s.findDuplicate([3, 1, 3, 4, 3]) == 3
