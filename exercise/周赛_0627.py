"""
给你两个正整数 n 和 k 。

如果正整数 i 满足 n % i == 0 ，那么我们就说正整数 i 是整数 n 的因子。

考虑整数 n 的所有因子，将它们 升序排列 。请你返回第 k 个因子。如果 n 的因子数少于 k ，请你返回 -1 。



示例 1：

输入：n = 12, k = 3
输出：3
解释：因子列表包括 [1, 2, 3, 4, 6, 12]，第 3 个因子是 3 。
示例 2：

输入：n = 7, k = 2
输出：7
解释：因子列表包括 [1, 7] ，第 2 个因子是 7 。
示例 3：

输入：n = 4, k = 4
输出：-1
解释：因子列表包括 [1, 2, 4] ，只有 3 个因子，所以我们应该返回 -1 。
示例 4：

输入：n = 1, k = 1
输出：1
解释：因子列表包括 [1] ，第 1 个因子为 1 。
示例 5：

输入：n = 1000, k = 3
输出：4
解释：因子列表包括 [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000] 。


提示：

1 <= k <= n <= 1000
"""
# from exercise.myUtils import timer
#
#
# class Solution:
#     @timer
#     def kthFactor(self, n: int, k: int) -> int:
#         temp = []
#         for i in range(1, n + 1):
#             if n % i == 0:
#                 temp.append(i)
#                 if len(temp) == k:
#                     return i
#         return -1
#
#
# s = Solution()
# assert s.kthFactor(n=12, k=3) == 3
# assert s.kthFactor(n=7, k=2) == 7
# assert s.kthFactor(n=4, k=4) == -1
# assert s.kthFactor(n=1, k=1) == 1
# assert s.kthFactor(n=1000, k=3) == 4
from typing import List

from exercise.myUtils import timer

"""
给你一个二进制数组 nums ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。

 

提示 1：

输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：

输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
示例 3：

输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
示例 4：

输入：nums = [1,1,0,0,1,1,1,0,1]
输出：4
示例 5：

输入：nums = [0,0,0]
输出：0
 

提示：

1 <= nums.length <= 10^5
nums[i] 要么是 0 要么是 1 。
"""

# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         temp = []
#         count = 1
#         nums = nums + [0]
#         zeroexitflag = False
#         for i in range(1, len(nums)):
#             if nums[i] == 0:
#                 if i < len(nums) - 1:
#                     zeroexitflag = True
#                 if nums[i - 1] == 1:
#                     temp.append(count)
#                     count = 0
#             else:
#                 if nums[i - 1] == 0:
#                     temp.append(-count)
#                     count = 0
#             count += 1
#         res = 0
#         for i in range(len(temp)):
#             if temp[i] > 0:
#                 res = max(res, temp[i])
#             elif temp[i] == -1:
#                 if i > 0 and temp[i - 1] > 0 and i < len(temp) - 1 and temp[i + 1] > 0:
#                     res = max(res, temp[i - 1] + temp[i + 1])
#         return res if zeroexitflag else res - 1
#
#
# s = Solution()
# assert s.longestSubarray([1, 1, 1]) == 2
# assert s.longestSubarray([1, 1, 0, 1]) == 3
# assert s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
# assert s.longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1]) == 4
# assert s.longestSubarray([0, 0, 0]) == 0
# assert s.longestSubarray([1, 1, 1, 0, 0, 1]) == 3
# assert s.longestSubarray([1, 1, 1, 0, 1]) == 4
# assert s.longestSubarray([0, 1, 1, 0, 1, 0]) == 3
# assert s.longestSubarray([0, 1, 1, 0]) == 2
"""
并行课程二
给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 dependencies 中， dependencies[i] = [xi, yi]  表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。

在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。

请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。

 

示例 1：



输入：n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
输出：3 
解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。
示例 2：



输入：n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
输出：4 
解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。
示例 3：

输入：n = 11, dependencies = [], k = 2
输出：6
 

提示：

1 <= n <= 15
1 <= k <= n
0 <= dependencies.length <= n * (n-1) / 2
dependencies[i].length == 2
1 <= xi, yi <= n
xi != yi
所有先修关系都是不同的，也就是说 dependencies[i] != dependencies[j] 。
题目输入的图是个有向无环图。
"""


class Solution:
    @timer
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        dict = {}
        for i in range(len(dependencies)):
            if dependencies[i][1] in dict:
                dict[dependencies[i][1]].append(dependencies[i][0])
            else:
                dict[dependencies[i][1]] = [dependencies[i][0]]
        s = [0] * (n + 1)
        maxdeep = 0
        for i in range(1, n + 1):
            if i not in dict:
                s[i] = 0
            else:
                temp = set(dict[i])
                count = 0
                while temp:
                    count += 1
                    curr = set()
                    for x in temp:
                        if x in dict:
                            curr = curr.union(set(dict[x]))
                    temp = curr
                s[i] = count
                maxdeep = max(maxdeep, count)
        s = s[1:]
        print(s)
        deep = [0] * (maxdeep + 1)
        for i in range(len(s)):
            deep[s[i]] += 1
        print(deep)
        res = 0
        for i in range(len(deep)):
            if deep[i] % k == 0:
                res += deep[i] // k
            else:
                res += deep[i] // k + 1
        return res


s = Solution()
assert s.minNumberOfSemesters(8, [[1, 6], [2, 7], [8, 7], [2, 5], [3, 4]], 3) == 3
assert s.minNumberOfSemesters(n=4, dependencies=[[2, 1], [3, 1], [1, 4]], k=2) == 3
assert s.minNumberOfSemesters(n=5, dependencies=[[2, 1], [3, 1], [4, 1], [1, 5]], k=2) == 4
assert s.minNumberOfSemesters(n=11, dependencies=[], k=2) == 6
assert s.minNumberOfSemesters(n=4, dependencies=[[2, 1], [4, 3]], k=2) == 2

