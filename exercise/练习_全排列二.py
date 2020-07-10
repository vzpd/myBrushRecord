"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
from typing import List

from exercise.myUtils import timer, comparelist


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # if not nums:
        #     return []
        # if len(nums) == 1:
        #     return [nums]
        # s = set()
        # ans = []
        # for arr in self.permuteUnique(nums[:-1]):
        #     for i in range(len(arr)):
        #         if arr[i] != nums[-1]:
        #             curr = arr[:]
        #             curr.insert(i, nums[-1])
        #             if tuple(curr) not in s:
        #                 ans.append(curr)
        #                 s.add(tuple(curr))
        #     arr.append(nums[-1])
        #     if tuple(arr) not in s:
        #         ans.append(arr)
        #         s.add(tuple(arr))
        #
        # return ans
        nums.sort()
        ans = []

        def next(pre, left):
            if not left:
                ans.append(pre)

            for i in range(len(left)):
                if i > 0 and left[i - 1] == left[i]:
                    continue
                next(pre + [left[i]], left[:i] + left[i + 1:])

        next([], nums)
        return ans


s = Solution()
assert comparelist(s.permuteUnique([1, 1, 2, 2]), [[2, 2, 1, 1], [2, 1, 2, 1], [2, 1, 1, 2], [1, 2, 2, 1], [1, 2, 1, 2],
                                                   [1, 1, 2, 2]])
assert comparelist(s.permuteUnique([1, 1, 2]), [[2, 1, 1], [1, 2, 1], [1, 1, 2]])
assert comparelist(s.permuteUnique([1, 2, 3]), [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]])
assert comparelist(s.permuteUnique([1, 1]), [[1, 1]])
assert comparelist(s.permuteUnique([1, 1, 1]), [[1, 1, 1]])
assert comparelist(s.permuteUnique([1]), [[1]])
assert comparelist(s.permuteUnique([]), [[]])
