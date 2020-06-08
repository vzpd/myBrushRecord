import collections
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def equationsPossible(self, equations: List[str]) -> bool:
        class cobj(object):
            def __init__(self, chr):
                self.objection = set()
                self.count = 1

        dict = {}
        dp = []
        for i in range(len(equations)):
            c0 = equations[i][0]
            c3 = equations[i][3]
            op = equations[i][1]
            if c0 in dict:
                i0 = dict[c0]
            else:
                dp.append(cobj(c0))
                dict[c0] = len(dp) - 1
                i0 = len(dp) - 1

            if c3 in dict:
                i3 = dict[c3]
            else:
                dp.append(cobj(c3))
                dict[c3] = len(dp) - 1
                i3 = len(dp) - 1

            o0, o3 = dp[i0], dp[i3]

            if op == '=':
                if o0 not in o3.objection or o3 not in o0.objection:
                    if i0 < i3:
                        dp[i0].objection |= dp[i3].objection
                        if o3.count == 1:
                            dict[c3] = i0
                            o0.count += 1
                        else:
                            dp[i3] = dp[i0]
                            o0.count += 1
                    else:
                        dp[i3].objection |= dp[i0].objection
                        if o0.count == 1:
                            dict[c0] = i3
                            o3.count += 1
                        else:
                            dp[i0] = dp[i3]
                            o3.count += 1
                else:
                    return False
            else:
                if o0 == o3:
                    return False
                else:
                    o0.objection.add(o3)
                    o3.objection.add(o0)
        return True


s = Solution()
assert s.equationsPossible(["b!=g", "k!=e", "c==k", "c==b", "d!=i", "d==k", "k!=c"]) is False
assert s.equationsPossible(["a==b", "b!=a"]) is False
assert s.equationsPossible(["b==a", "a==b"]) is True
assert s.equationsPossible(["a==b", "b==c", "a==c"]) is True
assert s.equationsPossible(["a==b", "b!=c", "c==a"]) is False
assert s.equationsPossible(["c==c", "b==d", "x!=z"]) is True
assert s.equationsPossible(['a==b', 'c==d', 'b==d', 'a!=c']) is False
