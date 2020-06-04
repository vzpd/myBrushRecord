# 给你一个整数数组 nums 和一个整数 k。
#
# 如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
#
# 请返回这个数组中「优美子数组」的数目。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,2,1,1], k = 3
# 输出：2
# 解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
# 示例 2：
#
# 输入：nums = [2,4,6], k = 1
# 输出：0
# 解释：数列中不包含任何奇数，所以不存在优美子数组。
# 示例 3：
#
# 输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# 输出：16
#  
#
# 提示：
#
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
from typing import List


class Solution:
    # 滑动窗口
    # @timer
    # def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    #     temp = [x % 2 for x in nums]
    #
    #     count, currCount, i, lenght = 0, 0, 0, len(temp)
    #     left, begin, end = 0, 0, 0
    #     indexList = []
    #
    #     while i < lenght:
    #         if temp[i] == 1:
    #             indexList.append(i)
    #             if currCount == 0:
    #                 begin = i
    #             currCount += 1
    #
    #         if currCount == k:
    #             end = i
    #             while i + 1 < lenght and temp[i + 1] == 0:
    #                 i += 1
    #             i += 1
    #
    #             count += (begin - left + 1) * (i - end)
    #             left = begin + 1
    #             begin = indexList[1 - k]
    #             currCount -= 1
    #         else:
    #             i += 1
    #
    #     return count

    # 将方法一滑动窗口解法优化，方法一中需反复查找满足条件的子序列左右两侧偶数的个数，
    # 现在直接将数组中的偶数去掉，将所有奇数的下标记录到新数组中，两侧偶数的个数直接用2子序列的下标减去相邻奇数的下标
    # def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    #     odd = [i for i in range(len(nums)) if nums[i] % 2]
    #     count = 0
    #     for i in range(k - 1, len(odd)):
    #         left, right = 0, 0
    #         if i - k + 1 > 0:
    #             left = odd[i - k + 1] - odd[i - k]
    #         else:
    #             left = odd[0] + 1
    #         if i + 1 < len(odd):
    #             right = odd[i + 1] - odd[i]
    #         else:
    #             right = len(nums) - odd[i]
    #         count += left * right
    #
    #     return count

    # 方法二继续优化如下，方法二中边界处理比较复杂，现在奇数下标数列前后各添加一个辅助位，
    # 同时更改循环起始位置，这样就不需要处理边界问题了
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = [i for i in range(len(nums)) if nums[i] % 2]
        odd = [-1] + odd + [len(nums)]
        count = 0
        for i in range(k, len(odd) - 1):
            left, right = 0, 0
            left = odd[i - k + 1] - odd[i - k]
            right = odd[i + 1] - odd[i]
            count += left * right

        return count


s = Solution()
assert s.numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2
assert s.numberOfSubarrays([1, 1, 1, 1, 1], 1) == 5
assert s.numberOfSubarrays([1, 1, 1, 1, 1], 2) == 4
assert s.numberOfSubarrays([2, 4, 6], 1) == 0
assert s.numberOfSubarrays([2, 1, 2, 2], 2) == 0
assert s.numberOfSubarrays([2, 1, 1, 2, 1, 1, 2], 2) == 9
assert s.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16
