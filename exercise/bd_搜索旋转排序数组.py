# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        begin, end = 0, len(nums) - 1
        while begin < end:
            if nums[begin] == target:
                return begin
            elif nums[end] == target:
                return end
            elif end - begin == 1:
                return -1
            else:
                half = (begin + end) // 2
                if nums[begin] < nums[half]:
                    if target in range(nums[begin], nums[half] + 1):
                        end = half
                    else:
                        begin = half
                if nums[half] < nums[end]:
                    if target in range(nums[half], nums[end] + 1):
                        begin = half
                    else:
                        end = half
        return -1


s = Solution()
assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert s.search([4, 5, 6, 7, 0], 3) == -1
assert s.search([4], 3) == -1
assert s.search([4], 4) == 0
