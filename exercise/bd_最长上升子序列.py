from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 暴力算法，遍历所有可能的组合
        # def findNext(i, pre):
        #     if i == len(nums):
        #         return 0
        #     len0, len1 = 0, 0
        #     if nums[i] > pre:
        #         len0 = findNext(i + 1, nums[i]) + 1
        #     len1 = findNext(i + 1, pre)
        #     return max(len0, len1)
        #
        # return findNext(0, -1)

        # 动态规划
        # if not nums:
        #     return 0
        # dp = [1]
        # for i in range(1, len(nums)):
        #     maxval = 0
        #     for j in range(0, i):
        #         if nums[i] > nums[j]:
        #             maxval = max(maxval, dp[j])
        #     dp.append(maxval + 1)
        #
        # return max(dp)

        # 动态规划+二分查找
        if not nums:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            maxval = 0
            # 天色已晚，并未改成二分法，待修改
            for j in range(len(dp)):
                if nums[i] > dp[j]:
                    maxval += 1
            if maxval == len(dp):
                dp.append(nums[i])
            else:
                dp[maxval] = dp[maxval] if dp[maxval] < nums[i] else nums[i]
        return len(dp)


s = Solution()
assert s.lengthOfLIS([10, 9, 2, 4, 5, 3, 7, 101, 18]) == 5
assert s.lengthOfLIS([10, 9, 2, 3]) == 2
