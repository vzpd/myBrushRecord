# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
#  
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
#  
#
# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
#
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # dict = {}
        # temp = 1
        # length = len(nums)
        # for i in range(length - 1):
        #     temp *= nums[i]
        #     dict[(0, i)] = temp
        # temp = 1
        # for i in range(length - 1, 0, -1):
        #     temp *= nums[i]
        #     dict[(i, length - 1)] = temp
        # res = [dict[(1, length - 1)]]
        # for i in range(1, length - 1):
        #     res.append(dict[(0, i - 1)] * dict[(i + 1, length - 1)])
        # res.append(dict[(1, length - 1)])
        # print(res)
        # return res
        l = len(nums)
        dp = [1] * l
        a = nums[0]
        b = nums[-1]
        for i in range(1, l):
            dp[i] *= a
            dp[l - 1 - i] *= b
            a *= nums[i]
            b *= nums[l - 1 - i]
        return dp


s = Solution()
assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
