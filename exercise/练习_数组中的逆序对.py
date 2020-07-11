"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
 

限制：

0 <= 数组长度 <= 50000
"""
import bisect
from typing import List

from exercise.myUtils import timer

"""
离散化树状数组
"""
class Solution:
    @timer
    def reversePairs(self, nums: List[int]) -> int:
        # count = 0
        #
        # def half(s, e):
        #     nonlocal count
        #     if s == e:
        #         return [nums[s]]
        #     mid = (s + e + 1) // 2
        #     left, right = half(s, mid - 1), half(mid, e)
        #     r = []
        #     i, j = 0, 0
        #     while i < len(left) and j < len(right):
        #         if left[i] > right[j]:
        #             r.append(right[j])
        #             j += 1
        #             count += len(left) - i
        #         else:
        #             r.append(left[i])
        #             i += 1
        #
        #     r += left[i:] + right[j:]
        #     return r
        #
        # if nums:
        #     half(0, len(nums) - 1)
        # return count
        if not nums:
            return 0
        cnums = sorted(nums)
        temp = [bisect.bisect_left(cnums, x) + 1 for x in nums]
        c = [0] * (len(nums) + 1)

        def lowbit(n):
            return n & (-n)

        def query(n):
            sum = 0
            while n > 0:
                sum += c[n]
                n -= lowbit(n)
            return sum

        def add(n):
            while n < len(c):
                c[n] += 1
                n += lowbit(n)

        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            ans += query(temp[i] - 1)
            add(temp[i])

        return ans


s = Solution()
assert s.reversePairs([5, 2, 6, 1]) == 4
assert s.reversePairs([1, 2, 5, 4, 7, 5, 63, 75, 48292])
assert s.reversePairs(
    [233, 2000000001, 234, 2000000006, 235, 2000000003, 236, 2000000007, 237, 2000000002, 2000000005, 233, 233, 233,
     233, 233, 2000000004])
assert s.reversePairs([7, 5, 6, 4, 8]) == 5
assert s.reversePairs([7, 5, 6, 4]) == 5
assert s.reversePairs([1]) == 0
assert s.reversePairs([]) == 0
assert s.reversePairs([1, 2, 3]) == 0
assert s.reversePairs([1, 2]) == 0
