from functools import lru_cache

from exercise.myUtils import timer

# 斐波那契数列
class Solution:
    @timer
    def translateNum(self, num: int) -> int:
        def cal(l):
            if l in dict:
                return dict[l]
            sum = 0
            residue = l // 2

            @lru_cache(10000)
            def getleft(c, gap):
                if c == 0 or gap == 0:
                    return 1
                else:
                    count = 0
                    for j in range(0, gap + 1):
                        count += getleft(c - 1, gap - j)
                    return count

            for i in range(residue + 1):
                sum += getleft(i, l - i * 2)

            return sum

        dict = {}
        index = 0
        pre = 1
        nums = [int(x) for x in str(num)]
        for i in range(len(nums)):
            if nums[i] not in (1, 2):
                if nums[i - 1] * 10 + nums[i] < 26:
                    pre *= cal(i - index + 1)
                elif i - index > 1:
                    pre *= cal(i - index)
                index = i + 1

        if len(nums) - index > 1:
            pre *= cal(len(nums) - index)

        return pre


s = Solution()
assert s.translateNum(1) == 1
assert s.translateNum(11) == 2
assert s.translateNum(111) == 3
assert s.translateNum(1111) == 5
assert s.translateNum(11111) == 8
assert s.translateNum(111111) == 13

assert s.translateNum(12123) == 8
assert s.translateNum(1212429444) == 8
assert s.translateNum(127) == 2
assert s.translateNum(817230807) == 4
assert s.translateNum(26) == 1
assert s.translateNum(1068385902) == 2
assert s.translateNum(1001) == 2
assert s.translateNum(136) == 2
assert s.translateNum(506) == 1
assert s.translateNum(624) == 2
assert s.translateNum(5217) == 3
assert s.translateNum(61134) == 3
assert s.translateNum(6113411) == 6
assert s.translateNum(11111111111111111111111111111) == 832040
