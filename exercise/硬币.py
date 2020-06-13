# 硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
#
# 示例1:
#
#  输入: n = 5
#  输出：2
#  解释: 有两种方式可以凑成总金额:
# 5=5
# 5=1+1+1+1+1
# 示例2:
#
#  输入: n = 10
#  输出：4
#  解释: 有四种方式可以凑成总金额:
# 10=10
# 10=5+5
# 10=5+1+1+1+1+1
# 10=1+1+1+1+1+1+1+1+1+1
# 说明：
#
# 注意:
#
# 你可以假设：
#
# 0 <= n (总金额) <= 1000000

from exercise.myUtils import timer


class Solution:
    @timer
    def waysToChange(self, n: int) -> int:
        coins = [1, 5, 10, 25]
        res = 0
        count25 = n // 25 + 1
        for i in range(count25):
            leftAfer25 = (n - i * 25)
            count10 = leftAfer25 // 10 + 1
            for j in range(count10):
                leftAfer10 = leftAfer25 - j * 10
                count5 = leftAfer10 // 5 + 1
                res += count5

        return res


s = Solution()
# assert s.waysToChange(1000000) == 242
assert s.waysToChange(1) == 1
assert s.waysToChange(5) == 2
assert s.waysToChange(10) == 4
assert s.waysToChange(15) == 6
assert s.waysToChange(20) == 9
assert s.waysToChange(25) == 13
assert s.waysToChange(30) == 18
assert s.waysToChange(35) == 24
assert s.waysToChange(40) == 31
assert s.waysToChange(45) == 39
assert s.waysToChange(50) == 49
assert s.waysToChange(55) == 60
assert s.waysToChange(60) == 73
assert s.waysToChange(65) == 87
assert s.waysToChange(5) == 2
assert s.waysToChange(10) == 4
assert s.waysToChange(11) == 4
assert s.waysToChange(25) == 13
assert s.waysToChange(20) == 9
assert s.waysToChange(30) == 18
assert s.waysToChange(40) == 31
assert s.waysToChange(61) == 73
assert s.waysToChange(500) == 19006
# assert s.waysToChange(1000000) == 84
