from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res ^= x
        return res


s = Solution()
assert s.singleNumber([1, 1, 0]) == 0
assert s.singleNumber([0, 1, 0]) == 1
assert s.singleNumber([2, 2, 1]) == 1
assert s.singleNumber([4, 1, 2, 1, 2]) == 4


# 面试题56 - I. 数组中数字出现的次数
# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        temp = 0
        tempRes = reduce(lambda x, y: x ^ y, nums)
        t = 1
        while t & tempRes != t:
            t <<= 1
        a, b = 0, 0
        for x in nums:
            if x & t == t:
                a ^= x
            else:
                b ^= x
        return [a, b]


s = Solution()
assert s.singleNumbers([4, 1, 4, 6]) == [1, 6]
assert s.singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]) == [10, 2]


# # 面试题56 - II. 数组中数字出现的次数 II
# # 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         pass
#
#
# assert s.singleNumbers([3, 4, 3, 3]) == 4
# assert s.singleNumbers([9, 1, 7, 9, 7, 9, 7]) == 1
