# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 示例 1:
#
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
# 示例 2:
#
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
import math

from exercise.myUtils import count_time


class Solution:
    @count_time
    def numSquares(self, n: int) -> int:
        # 暴力枚举
        # @lru_cache(10000)
        # def getLeft(n: int):
        #     x = pow(n, 0.5)
        #     y = int(x)
        #     if x == y:
        #         return 1
        #     else:
        #         res = sys.maxsize
        #         for i in range(y, y // 2, -1):
        #             r = 1 + getLeft(n - i * i)
        #             res = min(res, r)
        #         return res
        #
        # return getLeft(n)

        # 动态规划

        # sqr = pow(n, 0.5)
        # if int(sqr) == sqr:
        #     return 1
        # sqrNum = [i * i for i in range(int(pow(n, 0.5)) + 1)]
        # dp = [0] + [float('inf')] * n
        # for i in range(1, n + 1):
        #     for j in [x for x in sqrNum if x <= i]:
        #         dp[i] = min(dp[i], dp[i - j] + 1)
        #
        # return dp[n]

        # 贪心枚举
        # @lru_cache(10000)
        # def isDividedBy(k, count) -> bool:
        #     if count == 1:
        #         return k in numSquares
        #     else:
        #         for num in numSquares:
        #             if isDividedBy(k - num, count - 1):
        #                 return True
        #         else:
        #             return False
        #
        # sqr = n ** 0.5
        # sqrInt = int(sqr)
        # if sqr == sqrInt:
        #     return 1
        # numSquares = [x ** 2 for x in range(1, sqrInt + 1)]
        #
        # for count in range(1, n + 1):
        #     if isDividedBy(n, count):
        #         return count

        # 贪心 + BFS
        # sqr = n ** 0.5
        # sqrInt = int(sqr)
        # if sqr == sqrInt:
        #     return 1
        #
        # numSquares = [x * x for x in range(1, sqrInt + 1)]
        #
        # count = 0
        # currDp = {n}
        # while 1:
        #     count += 1
        #     nextDp = set()
        #     for x in currDp:
        #         sqr = x ** 0.5
        #         if sqr == int(sqr):
        #             return count
        #         else:
        #             for y in [y for y in numSquares if y < x]:
        #                 nextDp.add(x - y)
        #     currDp = nextDp

        # 数学运算
        def isSquare(n: int) -> bool:
            sq = int(math.sqrt(n))
            return sq * sq == n

        # four-square and three-square theorems
        while (n & 3) == 0:
            n >>= 2  # reducing the 4^k factor from number
        if (n & 7) == 7:  # mod 8
            return 4
        if isSquare(n):
            return 1
        # check if the number can be decomposed into sum of two squares
        for i in range(1, int(n ** (0.5)) + 1):
            if isSquare(n - i * i):
                return 2
        # bottom case from the three-square theorem
        return 3


s = Solution()
assert s.numSquares(12) == 3
assert s.numSquares(14) == 3
assert s.numSquares(13) == 2
assert s.numSquares(15) == 4
assert s.numSquares(20) == 2
assert s.numSquares(37) == 2
assert s.numSquares(42) == 3
assert s.numSquares(48) == 3
assert s.numSquares(108) == 3
assert s.numSquares(2536) == 2
assert s.numSquares(100000000) == 1
