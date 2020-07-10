# 你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。
# 例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。
# 但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。
#
# 示例 1：
# 输入： pattern = "abba", value = "dogcatcatdog"
# 输出： true
# 示例 2：
# 输入： pattern = "abba", value = "dogcatcatfish"
# 输出： false
# 示例 3：
# 输入： pattern = "aaaa", value = "dogcatcatdog"
# 输出： false
# 示例 4：
# 输入： pattern = "abba", value = "dogdogdogdog"
# 输出： true
# 解释： "a"="dogdog",b=""，反之也符合规则
# 提示：
# 0 <= len(pattern) <= 1000
# 0 <= len(value) <= 1000
# 你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。
import collections

from exercise.myUtils import timer

"""
此题解法不难想出，但是难在设定a、b都可以空，且a不能等于b
因此边界条件判断需要非常细心
"""
class Solution:
    @timer
    def patternMatching(self, pattern: str, value: str) -> bool:
        counter = collections.Counter(pattern)
        chrA, chrB = 'a', 'b'
        if counter[chrA] < counter[chrB]:
            chrA, chrB = chrB, chrA
        if counter[chrA] == 0:
            return value == ''
        for i in range(len(value) // counter[chrA] + 1):
            al = i
            bl = (len(value) - al * counter[chrA]) // counter[chrB] if counter[chrB] > 0 else 0
            a, b, index = None, None, 0
            for j in range(len(pattern)):
                if pattern[j] == chrA:
                    if a is None:
                        a = value[index:index + al]
                    else:
                        temp = value[index:index + al]
                        if a != temp:
                            break
                    index += al
                else:
                    if b is None:
                        b = value[index: index + bl]
                    else:
                        temp = value[index: index + bl]
                        if b != temp:
                            break
                    index += bl
                if a is not None and b is not None and a == b:
                    break
            if index == len(value) and a != b:
                return True

        return False


s = Solution()
assert s.patternMatching('ab', '') is False
assert s.patternMatching(pattern="abba", value="dogdogdogdog") is True
assert s.patternMatching(pattern="aaaa", value="dogcatcatdog") is False
assert s.patternMatching(pattern="abba", value="dogcatcatdog") is True
assert s.patternMatching('', '') is True
assert s.patternMatching('a', '') is True
assert s.patternMatching('', 'a') is False
assert s.patternMatching(pattern="abba", value="dogcatcatfish") is False
assert s.patternMatching(pattern="bbbb", value="dogcatcatdog") is False
