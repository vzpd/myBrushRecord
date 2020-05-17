import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS
        # dictFrom = {}
        # for x in prerequisites:
        #     if x[1] in dictFrom:
        #         dictFrom[x[1]].append(x[0])
        #     else:
        #         dictFrom[x[1]] = [x[0]]
        # res = []
        # visited = [0] * numCourses
        # invalid = False
        #
        # def find(i):
        #     nonlocal invalid
        #     visited[i] = 1
        #     temp = dictFrom.get(i)
        #     if temp:
        #         for j in temp:
        #             if visited[j] == 0:
        #                 find(j)
        #                 if invalid:
        #                     return
        #             elif visited[j] == 1:
        #                 invalid = True
        #                 return
        #     visited[i] = 2
        #     res.append(i)
        #
        # for i in range(numCourses):
        #     if not invalid and visited[i] == 0:
        #         find(i)
        # if invalid:
        #     return list()
        # return res[::-1]
        # BFS
        # 存储有向图
        # 存储有向图
        edges = collections.defaultdict(list)
        # 存储每个节点的入度
        indeg = [0] * numCourses
        # 存储答案
        result = list()

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        # 将所有入度为 0 的节点放入队列中
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            # 从队首取出一个节点
            u = q.popleft()
            # 放入答案中
            result.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
                if indeg[v] == 0:
                    q.append(v)

        if len(result) != numCourses:
            result = list()
        return result


s = Solution()
assert s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in ([0, 1, 2, 3], [0, 2, 1, 3])
assert s.findOrder(2, [[0, 1]]) == [1, 0]
assert s.findOrder(2, [[0, 1], [1, 0]]) == []
assert s.findOrder(5, [[1, 0], [4, 1], [2, 1], [3, 2], [2, 3]]) == []
assert s.findOrder(2, [[1, 0]]) == [0, 1]
