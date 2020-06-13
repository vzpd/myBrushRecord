from exercise.myUtils import timer


class Solution:
    @timer
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        elif n == 0:
            return 1

        dp = [1]
        dpRes = [x]
        while dp[-1] * 2 < n:
            dp.append(dp[-1] * 2)
            dpRes.append(dpRes[-1] * dpRes[-1])

        res = 1
        left = n
        index = len(dp) - 1
        while left:
            if left < dp[index]:
                index -= 1
            else:
                left -= dp[index]
                res *= dpRes[index]
        return res


s = Solution()
assert s.myPow(0.86429, 18) == 0.0724220454880128
assert s.myPow(8.84372, -5)
assert s.myPow(1, 1) == 1
assert s.myPow(1, 0) == 1
assert s.myPow(2, 10) == 1024
assert s.myPow(0.00001, 21474836415617) == 0.0
assert s.myPow(2, 3) == 8
assert s.myPow(2.10000, 3) == 9.261000000000001
assert s.myPow(2, -2) == 0.25000
# assert s.myPow(100, 2 ** 31 - 1)
