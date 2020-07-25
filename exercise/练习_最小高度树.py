import collections
from typing import List

from exercise.myUtils import timer

"""
只要找到最长的那条路径，返回最中间位置的节点即可。

我们将路径记录到graph这个dict中

然后从所有叶子节点开始BFS，
从节点i到达下一个节点j时，
    我们直接从graph[j]中将前一个节点i移除，
    然后判断j的剩余连接数，如果大于1，
        则表明我们当前所在树枝不是节点j连接的最长树枝，
        因为越短的枝，越早到达交汇处
        我们终止遍历，将此树枝舍弃掉
    如果连接数为1，
        则表明我们当前所在的树枝，有可能是最长的那个
        将j添加到下一轮的遍历中
最后，我们找不到下一轮的节点了
至此我们已经树上的所有节点遍历完成
返回这轮的所有节点即可
"""


class Solution:
    @timer
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # graph = collections.defaultdict(list)
        # for p, q in edges:
        #     graph[p].append(q)
        #     graph[q].append(p)
        #
        # nodes = []
        # degrees = [0] * n
        # for i in range(n):
        #     degrees[i] = len(graph[i])
        #     if len(graph[i]) <= 1:
        #         nodes.append(i)
        #
        # while True:
        #     temp = []
        #     for i in nodes:
        #         for j in graph[i]:
        #             if degrees[j] == 2:
        #                 temp.append(j)
        #             if degrees[j] >= 2:
        #                 degrees[j] -= 1
        #     if not temp:
        #         return nodes
        #     nodes = temp
        graph = collections.defaultdict(set)
        for p, q in edges:
            graph[p].add(q)
            graph[q].add(p)

        nodes = []
        for i in range(n):
            if len(graph[i]) < 2:
                nodes.append(i)

        while True:
            temp = []
            for i in nodes:
                for j in graph[i]:
                    graph[j].remove(i)
                    if len(graph[j]) == 1:
                        temp.append(j)
            if not temp:
                return nodes
            nodes = temp


s = Solution()
assert s.findMinHeightTrees(1, []) == [0]
assert s.findMinHeightTrees(7, [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == [1, 2]
assert s.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]) == [1]
assert s.findMinHeightTrees(n=6, edges=[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]) == [3, 4]
