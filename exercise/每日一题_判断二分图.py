import collections
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        temp = [-1] * len(graph)
        valid = True

        def track(n, type):
            nonlocal valid
            temp[n] = type
            for x in graph[n]:
                if temp[x] == -1:
                    track(x, type ^ 1)
                elif temp[x] != type ^ 1:
                    valid = False
                    break

        for i in range(len(graph)):
            if temp[i] == -1:
                track(i, 1)
                if not valid:
                    return False

        return True


s = Solution()
assert s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True
assert s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False
