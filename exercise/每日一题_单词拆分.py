"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
import collections
from typing import List

from exercise.myUtils import timer

'''
动态规划：
    如果s[:j]由wordDict中到元素组成，并且s[j:i]是wordDict中到元素，
    那么s[:i]就可以由wordDict中到元素组成，
    依次递推，最后可以判断s是否由wordDict中到元素组成
'''


class Solution:
    @timer
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp = set([''])
        # while True:
        #     temp = set()
        #     for x in dp:
        #         for y in wordDict:
        #             if len(x + y) <= len(s) and s.startswith(x + y):
        #                 if x + y == s:
        #                     return True
        #                 temp.add(x + y)
        #     if temp:
        #         dp = temp
        #     else:
        #         return False
        # temp = set()
        # for i in range(len(wordDict)):
        #     for j in range(len(s) - len(wordDict[i]) + 1):
        #         if s[j:].startswith(wordDict[i]):
        #             temp.add((j, j + len(wordDict[i])))
        #
        # l = list([list(x) for x in temp])
        # l.sort()
        # temp = {0}
        # for i in range(len(l)):
        #     if l[i][0] in temp:
        #         if l[i][1] == len(s):
        #             return True
        #         temp.add(l[i][1])
        #
        # return False
        # dp = {0}
        # while True:
        #     temp = set()
        #     for i in dp:
        #         for j in range(len(wordDict)):
        #             if i + len(wordDict[j]) <= len(s):
        #                 if s[i:].startswith(wordDict[j]):
        #                     temp.add(i + len(wordDict[j]))
        #                     if i + len(wordDict[j]) == len(s):
        #                         return True
        #     if temp:
        #         dp = temp
        #     else:
        #         return False
        words = set(wordDict)
        dp = [True]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp.append(True)
                    break
            else:
                dp.append(False)
        return dp[-1]


s = Solution()
assert s.wordBreak(s="leetcode", wordDict=["leet", "code"]) is True
assert s.wordBreak("dogs", ["dog", "s", "gs"]) is True
assert s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]) is False
assert s.wordBreak(s="applepenapple", wordDict=["apple", "pen"]) is True
assert s.wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    , ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]) is False
