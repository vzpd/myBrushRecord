# 暴力方法：
# 双重循环遍历所有子字符串中元音字母出现的次数，
# 符合要求则更新最长子字符串的长度，
# 最后返回符合要求的子字符串长度最大值
# 问题：超时
#
# 优化一：前缀和
# j>i,判断子字符串s[i,j]中元音字母出现的次数是否都为偶数，
# 只需要用s[:j]中每个元音字母出现次数减去s[:i-1]中每个元音字母次数，
# 然后判断每个差值是否都为偶数
# 如果都为偶数则子字符串符合要求
# 问题：虽然减少了计算每个子字符串中元音字母出现的次数的步骤，
# 但是遍历j的时候能否直接找到i(j>i),使得s[i,j]满足要求，
# 从而使得时间复杂度降低到O(n)？
#
# 优化二：状态压缩
# 我们可以把元音字母出现的次数进行状态压缩，
# 可以用0表示元音字母出现偶数次，1表示元音字母出现奇数次，
# 5个元音字母出现的奇偶次数可以用5位的二进制数表示，
# 例如s[:i-1]为10000表示u出现奇数次，其他4个元音字母都出现偶数次
# 偶数减去偶数，差值为偶数，奇数减去奇数，差值也为偶数，
# 如果s[:j]也为10000,则s[i:j]中每个元音字母出现次数均为偶数次，
# s[i:j]为符合条件的子字符串，
# j-i为其长度
# 因此只需记录每种状态status第一次出现的位置，
# 这里用dict记录每种状态第一次出现的位置
# 后面再次出现的话与第一次出现的位置的差值即为符合条件的子字符串的长度
# 我们用status表示第i位的所有元音出现次数的状态
# status二进制从右往左第一到第五位分表表示a、e、i、o、u出现的次数的奇偶情况
# 如果第s[i]为元音字母a，要求现在的status，
# 我们用s[i-1]的status在第一位取反，
# 即可获得当前的status
# 然后我们在dict中寻找status
# 如果找到，则下标相减，得到符合条件的子字符串的长度，更新最大长度
# 如果未找到，则记录到dict中。
# 时间复杂度为O(n)

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dict = {0: -1}
        status, maxLength = 0, 0
        for i in range(len(s)):
            if s[i] == 'a':
                status ^= 1 << 0
            elif s[i] == 'e':
                status ^= 1 << 1
            elif s[i] == 'i':
                status ^= 1 << 2
            elif s[i] == 'o':
                status ^= 1 << 3
            elif s[i] == 'u':
                status ^= 1 << 4
            if status in dict:
                maxLength = max(maxLength, i - dict[status])
            else:
                dict[status] = i
        return maxLength


s = Solution()
assert s.findTheLongestSubstring('eleetminicoworoep') == 13
assert s.findTheLongestSubstring('leetcodeisgreat') == 5
assert s.findTheLongestSubstring('bcbcbc') == 6
