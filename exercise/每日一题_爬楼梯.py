class Solution:
    def climbStairs(self, n: int) -> int:
        # if n < 1:
        #     return 0
        # dp = [1, 2]
        # for i in range(2, n):
        #     dp.append(dp[-1] + dp[-2])
        #
        # return dp[n - 1]
        if n < 1:
            return 0
        a, b = 1, 1
        for i in range(1, n):
            b, a = a + b, b

        return b


s = Solution()
assert s.climbStairs(1) == 1
assert s.climbStairs(2) == 2
assert s.climbStairs(3) == 3
assert s.climbStairs(4) == 5
assert s.climbStairs(0) == 0
