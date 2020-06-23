# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
# 输入为 非空 字符串且只包含数字 1 和 0。
#
#  
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#  
#
# 提示：
#
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
from exercise.myUtils import timer

'''
注意：
    1、数字是从右往左做加法，而不是从左往右
    2、检查最后有没有进位
'''


class Solution:
    @timer
    def addBinary(self, a: str, b: str) -> str:
        # res, i, pre = '', -1, 0
        # l, al, bl = -max(len(a), len(b)), -len(a), -len(b)
        # while i >= l:
        #     ca = int(a[i]) if i >= al else 0
        #     cb = int(b[i]) if i >= bl else 0
        #     sum = ca + cb + pre
        #     res = str(sum % 2) + res
        #     pre = 1 if sum > 1 else 0
        #     i -= 1
        # return res if pre == 0 else '1' + res
        x, y = int(a, 2), int(b, 2)
        while y:
            # answer保留x于y相加之后每一位上的结果
            answer = x ^ y
            # carry保留x于y相加之后每一位上的进位，将所有的进位左移一位，是为了把所有进位加到answer上
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


s = Solution()
assert s.addBinary(a="1010", b="1011") == "10101"
assert s.addBinary(a="11", b="1") == "100"
assert s.addBinary(a="11", b="0") == "11"
assert s.addBinary(a="0", b="111") == "111"
assert s.addBinary(a="111", b="1") == "1000"
assert s.addBinary(a="1", b="111") == "1000"
assert s.addBinary('1111111', '10') == '10000001'
