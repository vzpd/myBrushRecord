# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
# 使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#  
#
# 示例：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
#
# 提示：
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            diff = target - nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                temp = nums[j] + nums[k]
                if abs(target - res) > abs(target - nums[i] - temp):
                    res = temp + nums[i]
                if diff > temp:
                    j += 1
                elif diff == temp:
                    return target
                else:
                    k -= 1

        return res


s = Solution()
assert s.threeSumClosest(nums=[-1, 2, 1, -4], target=1) == 2
assert s.threeSumClosest(nums=[1, 1, 1], target=1) == 3
assert s.threeSumClosest(nums=[1, 1, -1], target=1) == 1
assert s.threeSumClosest(nums=[1, 1, -2], target=1) == 0
assert s.threeSumClosest(nums=[1, 1, -1, 1], target=1) == 1
assert s.threeSumClosest(nums=[1, 1, -2, 1], target=1) == 0
