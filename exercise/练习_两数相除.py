"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

 

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
 

提示：

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
"""

"""
位运算，模拟除法过程。
"""
from exercise.myUtils import timer


class Solution:
    @timer
    def divide(self, dividend: int, divisor: int) -> int:
        deflag, diflag = dividend >= 0, divisor >= 0
        dividend = dividend if deflag else - dividend
        divisor = divisor if diflag else -divisor

        c = 0
        while dividend > divisor:
            divisor <<= 1
            c += 1

        res = 0
        while c >= 0:
            res <<= 1
            if dividend >= divisor:
                res ^= 1
                dividend -= divisor
            divisor >>= 1
            c -= 1
        res = -res if diflag ^ deflag else res
        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res
        else:
            return 2 ** 31 - 1


s = Solution()
assert s.divide(-2147483648, 1) == -2147483648
assert s.divide(dividend=10, divisor=3) == 3
assert s.divide(dividend=7, divisor=-3) == -2
assert s.divide(10, -2) == -5
assert s.divide(-10, 3) == -3
assert s.divide(-15, -4) == 3
assert s.divide(3, 10) == 0
assert s.divide(-3, 10) == 0
assert s.divide(17, 2) == 8
