# 求 1+2+...+n ，
# 要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
class Solution:
    # def sumNums(self, n: int) -> int:
    #     def sum(n):
    #         nonlocal res
    #         n > 0 and sum(n - 1)
    #         res += n
    #
    #     res = 0
    #     sum(n)
    #     return res
    def sumNums(self, n: int) -> int:
        temp = 1 << 27
        part = n + 1
        res = 0

        def next():
            nonlocal temp, res, n, part
            # a = temp - (n & 1)
            # res += part & a
            n & 1 and (res := res + part)
            n >>= 1
            part <<= 1

        next()
        next()
        next()
        next()
        next()
        next()
        next()
        next()
        next()
        next()
        next()
        next()
        next()
        next()

        return res >> 1


s = Solution()
assert s.sumNums(1) == 1
assert s.sumNums(2) == 3
assert s.sumNums(3) == 6
assert s.sumNums(4) == 10
assert s.sumNums(5) == 15
assert s.sumNums(6) == 21
assert s.sumNums(7) == 28
assert s.sumNums(8) == 36
assert s.sumNums(9) == 45
assert s.sumNums(10) == 55
assert s.sumNums(11) == 66
assert s.sumNums(50) == 1275
assert s.sumNums(80) == 3240
assert s.sumNums(100) == 5050
assert s.sumNums(150) == 11325
assert s.sumNums(200) == 20100
assert s.sumNums(500) == 125250
assert s.sumNums(1000) == 500500
assert s.sumNums(10000) == 50005000
