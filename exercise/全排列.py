# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
from typing import List

from exercise.myUtils import count_time


class Solution:
    @count_time
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     def combo(pre: List, numsLeft: List):
    #         length = len(numsLeft)
    #         if length == 0:
    #             return
    #         if length == 1:
    #             res.append(pre + numsLeft)
    #             return
    #
    #         for i in range(length):
    #             temp = numsLeft[:]
    #             x = temp.pop(i)
    #             combo(pre + [x], temp)
    #
    #     res = []
    #
    #     combo([], nums)
    #     return res
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length == 0:
            return []
        res = [[nums[0]]]
        for i in range(1, length):
            for j in range(len(res)):
                curr = res[j][:]
                res[j].append(nums[i])
                for k in range(1, len(res[j]) - 1):
                    temp = curr[:]
                    temp.insert(k, nums[i])
                    res.append(temp)

        for i in range(len(res)):
            x = res[i]
            for j in range(1, length):
                res.append(x[j:] + x[:j])

        # print(res)

        return res


s = Solution()
assert s.permute([]) == []
assert s.permute([1]) == [[1]]
assert s.permute([1, 2, 3])  # == [
#     [1, 2, 3],
#     [1, 3, 2],
#     [2, 1, 3],
#     [2, 3, 1],
#     [3, 1, 2],
#     [3, 2, 1]
# ]
assert s.permute([1, 2, 3, 4, 5])
assert s.permute([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# assert s.permute([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
