import collections
from typing import List

from exercise.myUtils import timer

# 并查集
class Solution:
    @timer
    def equationsPossible(self, equations: List[str]) -> bool:
        # class cobj(object):
        #     def __init__(self, chr):
        #         self.objection = set()
        #         self.count = 1
        #
        # dict = {}
        # dp = []
        # for i in range(len(equations)):
        #     c0 = equations[i][0]
        #     c3 = equations[i][3]
        #     op = equations[i][1]
        #     if c0 in dict:
        #         i0 = dict[c0]
        #     else:
        #         dp.append(cobj(c0))
        #         dict[c0] = len(dp) - 1
        #         i0 = len(dp) - 1
        #
        #     if c3 in dict:
        #         i3 = dict[c3]
        #     else:
        #         dp.append(cobj(c3))
        #         dict[c3] = len(dp) - 1
        #         i3 = len(dp) - 1
        #
        #     o0, o3 = dp[i0], dp[i3]
        #
        #     if op == '=':
        #         if o0 not in o3.objection or o3 not in o0.objection:
        #             if i0 < i3:
        #                 dp[i0].objection |= dp[i3].objection
        #                 if o3.count == 1:
        #                     dict[c3] = i0
        #                     o0.count += 1
        #                 else:
        #                     dp[i3] = dp[i0]
        #                     o0.count += 1
        #             else:
        #                 dp[i3].objection |= dp[i0].objection
        #                 if o0.count == 1:
        #                     dict[c0] = i3
        #                     o3.count += 1
        #                 else:
        #                     dp[i0] = dp[i3]
        #                     o3.count += 1
        #         else:
        #             return False
        #     else:
        #         if o0 == o3:
        #             return False
        #         else:
        #             o0.objection.add(o3)
        #             o3.objection.add(o0)
        # return True
        class cobj(object):
            def __init__(self):
                self.objection = set()
                self.count = 1

        def create(c):
            dp.append(cobj())
            dict[c] = len(dp) - 1
            return dp[-1]

        dict = {}
        dp = []
        for i in range(len(equations)):
            c0 = equations[i][0]
            c3 = equations[i][3]
            op = equations[i][1]
            if op == '=':
                if c0 == c3:
                    continue
                if c0 in dict and c3 in dict:
                    i0, i3 = dict[c0], dict[c3]
                    o0, o3 = dp[i0], dp[i3]
                    if o0 not in o3.objection and o3 not in o0.objection:
                        if i0 < i3:
                            if o3.count == 1:
                                dict[c3] = i0
                            else:
                                dp[i3] = dp[i0]
                            o0.objection |= o3.objection
                        else:
                            if o0.count == 1:
                                dict[c0] = i3
                            else:
                                dp[i0] = dp[i3]
                            o3.objection |= o0.objection
                    else:
                        return False
                elif c0 in dict:
                    i0 = dict[c0]
                    dict[c3] = i0
                    dp[i0].count += 1
                elif c3 in dict:
                    i3 = dict[c3]
                    dict[c0] = i3
                    dp[i3].count += 1
                else:
                    dp.append(cobj())
                    dict[c0] = len(dp) - 1
                    dict[c3] = len(dp) - 1
                    dp[-1].count += 1
            else:
                if c0 == c3:
                    return False
                if c0 in dict and c3 in dict:
                    i0, i3 = dict[c0], dict[c3]
                    o0, o3 = dp[i0], dp[i3]
                    if o0 == o3:
                        return False
                elif c0 in dict:
                    i0 = dict[c0]
                    o0 = dp[i0]
                    o3 = create(c3)
                    o0.objection.add(o3)
                    o3.objection.add(o0)
                elif c3 in dict:
                    i3 = dict[c3]
                    o3 = dp[i3]
                    o0 = create(c0)
                    o0.objection.add(o3)
                    o3.objection.add(o0)
                else:
                    o0 = create(c0)
                    o3 = create(c3)
                    o0.objection.add(o3)
                    o3.objection.add(o0)

        return True


s = Solution()
assert s.equationsPossible(["a!=b", "b!=c", "c!=a"]) is True
assert s.equationsPossible(["b!=g", "k!=e", "c==k", "c==b", "d!=i", "d==k", "k!=c"]) is False
assert s.equationsPossible(["a==b", "b!=a"]) is False
assert s.equationsPossible(["b==a", "a==b"]) is True
assert s.equationsPossible(["a==b", "b==c", "a==c"]) is True
assert s.equationsPossible(["a==b", "b!=c", "c==a"]) is False
assert s.equationsPossible(["c==c", "b==d", "x!=z"]) is True
assert s.equationsPossible(['a==b', 'c==d', 'b==d', 'a!=c']) is False
assert s.equationsPossible(['a!=a']) is False
assert s.equationsPossible(
    ["q==j", "d!=n", "u==a", "o!=e", "e==l", "q==s", "q!=h", "h!=w", "q!=n", "k==q", "m==k", "h!=u", "l==i", "b!=d",
     "a!=x", "c==h", "f!=k", "r==u", "o!=r", "n!=t", "p==n", "o!=m", "m!=w", "b!=f", "h!=o", "v==v", "j!=b", "k!=n",
     "w!=a", "i!=x", "o!=q", "u!=n", "i!=c", "q!=c", "p!=f", "u!=t", "a==r", "h!=k", "y==y", "r==o"]) is False
