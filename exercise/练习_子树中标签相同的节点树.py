import collections
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # graph = collections.defaultdict(list)
        # for p, q in edges:
        #     graph[p].append(q)
        #     graph[q].append(p)
        #
        # ans = [0] * n
        # leaves = []
        # for i in range(n):
        #     if len(graph[i]) == 1:
        #         leaves.append(i)
        #
        # temp = [collections.defaultdict(int) for _ in range(n)]
        # def track(x, d):
        #     next = [y for y in graph[x] if ans[y] == 0]
        #     if (len(next) == 1 and x != 0) or (x == 0 and not next):
        #         for k, v in temp[x].items():
        #             d[k] += v
        #         d[labels[x]] += 1
        #         ans[x] = d[labels[x]]
        #         if next:
        #             track(next[0], d)
        #     else:
        #         for k, v in d.items():
        #             temp[x][k] += v
        #
        # for x in leaves:
        #     track(x, collections.defaultdict(int))
        #
        # return ans
        graph = collections.defaultdict(list)
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)

        ans = [0] * n
        d = collections.defaultdict(list)
        visit = [0] * n

        def track(x):
            visit[x] = 1
            d[labels[x]].append([x, 1])
            for y in graph[x]:
                if visit[y] == 0:
                    track(y)
            a, b = d[labels[x]].pop()
            ans[a] = b
            if d[labels[x]]:
                d[labels[x]][-1][1] += b

        track(0)

        return ans


s = Solution()
assert s.countSubTrees(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], labels="abaedcd") == [2, 1, 1, 1, 1,
                                                                                                          1, 1]
assert s.countSubTrees(n=4, edges=[[0, 1], [1, 2], [0, 3]], labels="bbbb") == [4, 2, 1, 1]
assert s.countSubTrees(n=5, edges=[[0, 1], [0, 2], [1, 3], [0, 4]], labels="aabab") == [3, 2, 1, 1, 1]
assert s.countSubTrees(n=6, edges=[[0, 1], [0, 2], [1, 3], [3, 4], [4, 5]], labels="cbabaa") == [1, 2, 1, 1, 2, 1]
assert s.countSubTrees(n=7, edges=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]], labels="aaabaaa") == [6, 5, 4, 1, 3,
                                                                                                          2, 1]
