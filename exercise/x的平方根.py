# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         left, right = 0, x
#         while int(left) != int(right):
#             temp = (left + right) / 2
#             if temp * temp > x:
#                 right = temp
#             else:
#                 left = temp
#         return int(left)

class Solution:
    def mySqrt(self, x: int) -> int:
        # 牛顿拉弗逊迭代法
        k = x // 2
        while True:
            if k * k <= x < (k + 1) * (k + 1):
                return k
            else:
                if k: k = (k + x // k) // 2
                else: k = 1

s = Solution()
assert s.mySqrt(8) == 2
assert s.mySqrt(4) == 2
assert s.mySqrt(1) == 1
