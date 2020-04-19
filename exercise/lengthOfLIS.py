# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
from typing import List

from exercise.myUtils import count_time


class Solution:
    @count_time
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[0,0]]
        for i in range(len(nums)):
            maxILength = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    maxILength = max(maxILength, dp[j] + 1)
            dp.append(maxILength)
        print(nums)
        print(dp)
        return max(dp + [0])


s = Solution()
assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 3, 4, 101, 18]) == 4
assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert s.lengthOfLIS([10]) == 1
assert s.lengthOfLIS([]) == 0
assert s.lengthOfLIS([10, 9, 2, 5, 3, 4]) == 3

[10, 9, 2, 5, 3, 7, 101, 18]
[0, 0, 0, 1, 1, 2, 3, 3]


[10, 9, 2, 5, 3, 7, 4, 5, 101, 18]
[ 1, 1, 1, 2, 2, 3, 3, 4,   5,  5]


[10, 9, 2, 5, 3, 7, 3, 4, 101, 18]
[ 1, 1, 1, 2, 2, 3, 2, 3,   4,  4]