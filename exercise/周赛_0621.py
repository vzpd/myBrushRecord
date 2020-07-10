# # # # 给你两个整数，n
# # # # 和
# # # # start 。
# # # #
# # # # 数组
# # # # nums
# # # # 定义为：nums[i] = start + 2 * i（下标从
# # # # 0
# # # # 开始）且
# # # # n == nums.length 。
# # # #
# # # # 请返回
# # # # nums
# # # # 中所有元素按位异或（XOR）后得到的结果。
# # # #
# # # #
# # # #
# # # # 示例
# # # # 1：
# # # #
# # # # 输入：n = 5, start = 0
# # # # 输出：8
# # # # 解释：数组
# # # # nums
# # # # 为[0, 2, 4, 6, 8]，其中(0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
# # # # "^"
# # # # 为按位异或
# # # # XOR
# # # # 运算符。
# # # # 示例
# # # # 2：
# # # #
# # # # 输入：n = 4, start = 3
# # # # 输出：8
# # # # 解释：数组
# # # # nums
# # # # 为[3, 5, 7, 9]，其中(3 ^ 5 ^ 7 ^ 9) = 8.
# # # # 示例
# # # # 3：
# # # #
# # # # 输入：n = 1, start = 7
# # # # 输出：7
# # # # 示例
# # # # 4：
# # # #
# # # # 输入：n = 10, start = 5
# # # # 输出：2
# # # #
# # # # 提示：
# # # #
# # # # 1 <= n <= 1000
# # # # 0 <= start <= 1000
# # # # n == nums.length
# # #
# # # # class Solution:
# # # #     def xorOperation(self, n: int, start: int) -> int:
# # # #         res = start
# # # #         for i in range(1, n):
# # # #             res ^= start + 2 * i
# # # #
# # # #         return res
# # # #
# # # #
# # # # s = Solution()
# # # # assert s.xorOperation(n=5, start=0) == 8
# # # 给你一个长度为
# # # n
# # # 的字符串数组
# # # names 。你将会在文件系统中创建
# # # n
# # # 个文件夹：在第
# # # i
# # # 分钟，新建名为
# # # names[i]
# # # 的文件夹。
# # #
# # # 由于两个文件
# # # 不能
# # # 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以(k)
# # # 的形式为新文件夹的文件名添加后缀，其中
# # # k
# # # 是能保证文件名唯一的
# # # 最小正整数 。
# # #
# # # 返回长度为
# # # n
# # # 的字符串数组，其中
# # # ans[i]
# # # 是创建第
# # # i
# # # 个文件夹时系统分配给该文件夹的实际名称。
# # #
# # #
# # #
# # # 示例
# # # 1：
# # #
# # # 输入：names = ["pes", "fifa", "gta", "pes(2019)"]
# # # 输出：["pes", "fifa", "gta", "pes(2019)"]
# # # 解释：文件系统将会这样创建文件名：
# # # "pes" --> 之前未分配，仍为
# # # "pes"
# # # "fifa" --> 之前未分配，仍为
# # # "fifa"
# # # "gta" --> 之前未分配，仍为
# # # "gta"
# # # "pes(2019)" --> 之前未分配，仍为
# # # "pes(2019)"
# # # 示例
# # # 2：
# # #
# # # 输入：names = ["gta", "gta(1)", "gta", "avalon"]
# # # 输出：["gta", "gta(1)", "gta(2)", "avalon"]
# # # 解释：文件系统将会这样创建文件名：
# # # "gta" --> 之前未分配，仍为
# # # "gta"
# # # "gta(1)" --> 之前未分配，仍为
# # # "gta(1)"
# # # "gta" --> 文件名被占用，系统为该名称添加后缀(k)，由于
# # # "gta(1)"
# # # 也被占用，所以
# # # k = 2 。实际创建的文件名为
# # # "gta(2)" 。
# # # "avalon" --> 之前未分配，仍为
# # # "avalon"
# # # 示例
# # # 3：
# # #
# # # 输入：names = ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]
# # # 输出：["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece(4)"]
# # # 解释：当创建最后一个文件夹时，最小的正有效
# # # k
# # # 为
# # # 4 ，文件名变为
# # # "onepiece(4)"。
# # # 示例
# # # 4：
# # #
# # # 输入：names = ["wano", "wano", "wano", "wano"]
# # # 输出：["wano", "wano(1)", "wano(2)", "wano(3)"]
# # # 解释：每次创建文件夹
# # # "wano"
# # # 时，只需增加后缀中
# # # k
# # # 的值即可。
# # # 示例
# # # 5：
# # #
# # # 输入：names = ["kaido", "kaido(1)", "kaido", "kaido(1)"]
# # # 输出：["kaido", "kaido(1)", "kaido(2)", "kaido(1)(1)"]
# # # 解释：注意，如果含后缀文件名被占用，那么系统也会按规则在名称后添加新的后缀(k) 。
# # #
# # #
# # # 提示：
# # #
# # # 1 <= names.length <= 5 * 10 ^ 4
# # # 1 <= names[i].length <= 20
# # # names[i]
# # # 由小写英文字母、数字和 / 或圆括号组成。
# # import collections
# # from typing import List
# #
# # from exercise.myUtils import timer
# #
# #
# # class Solution:
# #     @timer
# #     def getFolderNames(self, names: List[str]) -> List[str]:
# #         # vals = set()
# #         # for i in range(len(names)):
# #         #     if names[i] in vals:
# #         #         begin, end = 1, len(names) - 1
# #         #
# #         #         while begin <= end:
# #         #             mid = (begin + end) // 2
# #         #             if names[i] + '(' + str(mid) + ')' in vals:
# #         #                 begin = mid + 1
# #         #             else:
# #         #                 end = mid - 1
# #         #         for j in range(1, begin):
# #         #             if names[i] + '(' + str(j) + ')' not in vals:
# #         #                 names[i] = names[i] + '(' + str(j) + ')'
# #         #                 break
# #         #         else:
# #         #             names[i] = names[i] + '(' + str(begin) + ')'
# #         #
# #         #     vals.add(names[i])
# #         # return names
# #         dict = {}
# #         vals = set()
# #         for i in range(len(names)):
# #             if names[i] in vals:
# #                 count = dict[names[i]] + 1 if names[i] in dict else 1
# #                 while names[i] + '(' + str(count) + ')' in vals:
# #                     count += 1
# #                 dict[names[i]] = count
# #                 names[i] = names[i] + '(' + str(count) + ')'
# #             else:
# #                 dict[names[i]] = 0
# #
# #             vals.add(names[i])
# #
# #         return names
# #
# #
# # s = Solution()
# # assert s.getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"])
# # assert s.getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)"]) == ["kaido", "kaido(1)", "kaido(2)", "kaido(1)(1)"]
# # assert s.getFolderNames(["pes", "fifa", "gta", "pes(2019)"]) == ["pes", "fifa", "gta", "pes(2019)"]
# # assert s.getFolderNames(["gta", "gta(1)", "gta", "avalon"]) == ["gta", "gta(1)", "gta(2)", "avalon"]
# # assert s.getFolderNames(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]) == ["onepiece",
# #                                                                                                    "onepiece(1)",
# #                                                                                                    "onepiece(2)",
# #                                                                                                    "onepiece(3)",
# #                                                                                                    "onepiece(4)"]
# 你的国家有无数个湖泊，所有湖泊一开始都是空的。当第
# n
# 个湖泊下雨的时候，如果第
# n
# 个湖泊是空的，那么它就会装满水，否则这个湖泊会发生洪水。你的目标是避免任意一个湖泊发生洪水。
#
# 给你一个整数数组
# rains ，其中：
#
# rains[i] > 0
# 表示第
# i
# 天时，第
# rains[i]
# 个湖泊会下雨。
# rains[i] == 0
# 表示第
# i
# 天没有湖泊会下雨，你可以选择
# 一个
# 湖泊并
# 抽干
# 这个湖泊的水。
# 请返回一个数组
# ans ，满足：
#
# ans.length == rains.length
# 如果
# rains[i] > 0 ，那么ans[i] == -1 。
# 如果
# rains[i] == 0 ，ans[i]
# 是你第
# i
# 天选择抽干的湖泊。
# 如果有多种可行解，请返回它们中的
# 任意一个 。如果没办法阻止洪水，请返回一个
# 空的数组 。
#
# 请注意，如果你选择抽干一个装满水的湖泊，它会变成一个空的湖泊。但如果你选择抽干一个空的湖泊，那么将无事发生（详情请看示例
# 4）。
#
#
#
# 示例
# 1：
#
# 输入：rains = [1, 2, 3, 4]
# 输出：[-1, -1, -1, -1]
# 解释：第一天后，装满水的湖泊包括[1]
# 第二天后，装满水的湖泊包括[1, 2]
# 第三天后，装满水的湖泊包括[1, 2, 3]
# 第四天后，装满水的湖泊包括[1, 2, 3, 4]
# 没有哪一天你可以抽干任何湖泊的水，也没有湖泊会发生洪水。
# 示例
# 2：
#
# 输入：rains = [1, 2, 0, 0, 2, 1]
# 输出：[-1, -1, 2, 1, -1, -1]
# 解释：第一天后，装满水的湖泊包括[1]
# 第二天后，装满水的湖泊包括[1, 2]
# 第三天后，我们抽干湖泊
# 2 。所以剩下装满水的湖泊包括[1]
# 第四天后，我们抽干湖泊
# 1 。所以暂时没有装满水的湖泊了。
# 第五天后，装满水的湖泊包括[2]。
# 第六天后，装满水的湖泊包括[1, 2]。
# 可以看出，这个方案下不会有洪水发生。同时， [-1, -1, 1, 2, -1, -1]
# 也是另一个可行的没有洪水的方案。
# 示例
# 3：
#
# 输入：rains = [1, 2, 0, 1, 2]
# 输出：[]
# 解释：第二天后，装满水的湖泊包括[1, 2]。我们可以在第三天抽干一个湖泊的水。
# 但第三天后，湖泊
# 1
# 和
# 2
# 都会再次下雨，所以不管我们第三天抽干哪个湖泊的水，另一个湖泊都会发生洪水。
# 示例
# 4：
#
# 输入：rains = [69, 0, 0, 0, 69]
# 输出：[-1, 69, 1, 1, -1]
# 解释：任何形如[-1, 69, x, y, -1], [-1, x, 69, y, -1]
# 或者[-1, x, y, 69, -1]
# 都是可行的解，其中
# 1 <= x, y <= 10 ^ 9
# 示例
# 5：
#
# 输入：rains = [10, 20, 20]
# 输出：[]
# 解释：由于湖泊
# 20
# 会连续下
# 2
# 天的雨，所以没有没有办法阻止洪水。
#
#
# 提示：
#
# 1 <= rains.length <= 10 ^ 5
# 0 <= rains[i] <= 10 ^ 9
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def avoidFlood(self, rains: List[int]) -> List[int]:
        temp = []
        res = [-1 for i in range(len(rains))]
        dict = {}
        for i in range(len(rains)):
            if rains[i] == 0:
                temp.append(i)
            else:
                if rains[i] in dict:
                    if len(temp) == 0:
                        return []
                    else:
                        rindex = dict[rains[i]]
                        j = 0
                        while j < len(temp):
                            if temp[j] >= rindex:
                                index = temp.pop(j)
                                res[index] = rains[i]
                                dict.pop(rains[i])
                                break
                            j += 1
                        else:
                            return []
                else:
                    dict[rains[i]] = i
        for j in range(len(temp)):
            res[temp[j]] = 1
        return res


s = Solution()
assert s.avoidFlood([0, 1, 1]) == []
assert s.avoidFlood([1, 2, 3, 4]) == [-1, -1, -1, -1]
assert s.avoidFlood([1, 2, 0, 0, 2, 1]) == [-1, -1, 2, 1, -1, -1]
assert s.avoidFlood([1, 2, 0, 1, 2]) == []
assert s.avoidFlood([69, 0, 0, 0, 69]) == [-1, 69, 1, 1, -1]
