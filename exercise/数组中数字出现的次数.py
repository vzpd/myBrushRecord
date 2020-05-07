# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
#
#  
#
# 示例 1：
#
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
# 示例 2：
#
# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]
#  
#
# 限制：
#
# 2 <= nums <= 10000


import collections
import functools
from typing import List

collections.Counter


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        print(ret)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]


s = Solution()
# assert s.singleNumbers([4, 1, 4, 6]) == [1, 6]
assert s.singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]) == [10, 2]
