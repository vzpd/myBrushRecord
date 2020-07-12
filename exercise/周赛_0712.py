# # from typing import List
# #
# #
# # class Solution:
# #     def numIdenticalPairs(self, nums: List[int]) -> int:
# #         d = {}
# #         count = 0
# #         for i in range(len(nums)):
# #             if nums[i] in d:
# #                 count += d[nums[i]]
# #                 d[nums[i]] += 1
# #             else:
# #                 d[nums[i]] = 1
# #         return count
# #
# #
# # s = Solution()
# # assert s.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
# class Solution:
#     def numSub(self, s: str) -> int:
#         temp = []
#         count = 0
#         s += '0'
#         for i in range(len(s)):
#             if s[i] == '1':
#                 count += 1
#             else:
#                 temp.append(count)
#                 count = 0
#         ans = 0
#         for x in temp:
#             ans += (1 + x) / 2 * x
#         return ans % (10 ** 9 + 7)
#
#
# s = Solution()
# assert s.numSub('0110111') == 9
# assert s.numSub('101') == 2
# assert s.numSub('111111') == 21
# assert s.numSub("000") == 0
import collections
from typing import List

from exercise.myUtils import timer

import sys

from exercise.testfile01 import returntest

sys.setrecursionlimit(9000000)


class Solution:
    @timer
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # d = collections.defaultdict(dict)
        # for i, [p, q] in enumerate(edges):
        #     d[p][q] = succProb[i]
        #     d[q][p] = succProb[i]
        #
        # ans = 0
        # dr = {}
        #
        # def next(path, n, r):
        #     if n not in dr:
        #         dr[n] = r
        #     elif r <= dr[n]:
        #         return
        #     else:
        #         dr[n] = r
        #
        #     nonlocal ans
        #     if n == end:
        #         ans = max(ans, r)
        #         return
        #     nextn = [[v, k] for k, v in d[n].items() if 1 << (k + 1) & path == 0]
        #     nextn.sort(reverse=True)
        #     for v, k in nextn:
        #         next(1 << (k + 1) ^ path, k, r * v)
        #
        # next(1 << (start + 1), start, 1)
        #
        # return ans
        ###################
        # d = collections.defaultdict(dict)
        # for i, [p, q] in enumerate(edges):
        #     d[p][q] = succProb[i]
        #     d[q][p] = succProb[i]
        #
        # ans = 0
        # dr = {}
        # pre = collections.deque()
        # pre.append([start, 1, 1 << start])
        # while pre:
        #     c, r, path = pre.popleft()
        #     if c in dr and dr[c] >= r:
        #         continue
        #     else:
        #         dr[c] = r
        #
        #     if c == end:
        #         ans = max(ans, r)
        #
        #     if r <= ans:
        #         continue
        #
        #     # next = [(v, k) for k, v in d[c].items()]
        #     # next.sort(reverse=True)
        #     # for v, k in next:
        #     #     if 1 << k & path == 0:
        #     #         pre.append([k, r * v, 1 << k ^ path])
        #     for k, v in d[c].items():
        #         if 1 << k & path == 0:
        #             pre.append([k, r * v, 1 << k ^ path])
        #
        # return ans
        # 用于标记节点是否已经访问过
        vis = [0] * n

        # 用于标记已经访问过的节点个数
        cnt = 0

        import heapq
        # 最大堆，用于dijkstra里每次寻找当前未访问的节点中最大概率的节点
        # 如果用普通队列，会超时，因为查找最大的时间复杂度是O(n)
        q = []
        heapq.heappush(q, (-1, start))

        # 生成graph，数据格式为： {node1 : [(node2, prob1-2), (node3, prob1-3)], node2: [(node1: prob1-2), (node3: prob2-3)]}
        graph = {}
        for i, item in enumerate(edges):
            s, e, p = item[0], item[1], succProb[i]

            graph.setdefault(s, []).append((e, p))
            graph.setdefault(e, []).append((s, p))

        # 循环查找每个节点
        while cnt < n:
            # 队列为空，还没有找到，说明没有路径
            if not q:
                return 0

            # 从最大堆中获取当前还没遍历过的节点里，概率最大的节点
            maxProb, maxIdx = heapq.heappop(q)
            while vis[maxIdx]:
                maxProb, maxIdx = heapq.heappop(q)

            # 找到终点，结束循环
            if maxIdx == end:
                return -maxProb

            # 将该节点设置为已访问状态
            vis[maxIdx] = True
            cnt += 1

            # 对于所有邻居节点，如果没有被访问过，放入队列
            for e in graph[maxIdx]:
                if not vis[e[0]]:
                    heapq.heappush(q, (maxProb * e[1], e[0]))

        return 0


s = Solution()
assert s.maxProbability(n=6, edges=[[0, 1], [1, 2], [1, 3], [1, 4], [3, 4], [3, 5]],
                        succProb=[1, 0.1, 0.2, 0.3, 0.4, 0.5], start=0,
                        end=5) == 0.1
assert s.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2) == 0.25000
assert s.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start=0, end=2) == 0.30000
assert s.maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start=0, end=2) == 0.00000
assert s.maxProbability(5,
                        [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
                        [0.37, 0.17, 0.93, 0.23, 0.39, 0.04],
                        3,
                        4) == 0.2139
a, b, c, d, e = returntest()
assert s.maxProbability(a, b, c, d, e)
