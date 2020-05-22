# 中心扩散法
# 如名，从第i点开始，同时向左和向右遍历
# 如果左右两边相同，则为回文字符串
# 回文字符串里字符数可以为奇数也可以为偶数
# 奇数的话，都从s[i]开始左右扩散
# 偶数的话，从s[i]向左扩散，从s[i+1]开始向右扩散
# 最后找到最长的回文字符串返回即可

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩散
        length = len(s)

        def expend(x, y):
            while -1 < x and y < length and s[x] == s[y]:
                x -= 1
                y += 1
            return x, y

        x, y = 0, 1
        for i in range(1, len(s) - 1):
            tx, ty = expend(i, i)
            if ty - tx > y - x:
                x, y = tx, ty
            tx, ty = expend(i, i + 1)
            if ty - tx > y - x:
                x, y = tx, ty
        return s[x + 1: y]


s = Solution()
assert s.longestPalindrome('babad') == 'bab'
assert s.longestPalindrome('cbbd') == 'bb'
