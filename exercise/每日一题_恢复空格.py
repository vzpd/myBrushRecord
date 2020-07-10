"""
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经
变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，
不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数

 

示例：

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
提示：

0 <= len(sentence) <= 1000
dictionary中总字符数不超过 150000。
你可以认为dictionary和sentence中只包含小写字母。
"""
import collections
from typing import List

from exercise.myUtils import timer

"""
动态规划
f(x) = min(f(y1),f(y1),f(y3)....)
如果y-x之间的字符串正好在dictionary之中，则，f(x)的值为f(y)，如果有多个y存在，则，f(x)的值为其中最小的那个
如果不存在y，则f(x)=f(x-1)+1
"""


class Solution:
    @timer
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dict = collections.defaultdict(list)
        for i in range(len(dictionary)):
            dict[dictionary[i][0]].append(dictionary[i])

        dp = [0] + [float('inf')] * len(sentence)
        sentence = ' ' + sentence
        for i in range(1, len(sentence)):
            if sentence[i] in dict:
                for x in dict[sentence[i]]:
                    if i + len(x) <= len(sentence) and sentence[i:i + len(x)] == x:
                        dp[i + len(x) - 1] = min(dp[i + len(x) - 1], dp[i - 1])

            dp[i] = min(dp[i - 1] + 1, dp[i])

        return dp[-1]


s = Solution()
assert s.respace(['look'], 'alooka') == 2
assert s.respace(dictionary=["looked", "just", "like", "her", "brother"],
                 sentence="jesslookedjustliketimherbrother") == 7
assert s.respace(['look', 'okk'], 'alooka') == 2
assert s.respace(['look', 'oka'], 'alooka') == 2
assert s.respace(['look', 'oka'], '') == 0
assert s.respace([], 'abc') == 3
assert s.respace(['abc', 'cd'], 'abcd') == 1
assert s.respace(['bcde', 'abc', 'def'], 'abcdef') == 0
assert s.respace(['bcdef', 'abc', 'efg'], 'abcdefg') == 1
assert s.respace(['bcdef', 'abc', 'efg'], '') == 0
assert s.respace([], '') == 0
assert s.respace([], 'abc') == 3
