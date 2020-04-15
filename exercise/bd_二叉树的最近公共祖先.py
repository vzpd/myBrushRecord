from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def getTree(l: List):
    dp = [None if x is None else TreeNode(x) for x in l]
    dp.insert(0, None)
    for i in range(len(dp)):
        if dp[i] is not None:
            if 2 * i < len((dp)):
                dp[i].left = dp[2 * i]
            if 2 * i + 1 < len(dp):
                dp[i].right = dp[2 * i + 1]
    return dp[1:]


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def getTheNode(root, p, q, p_flag, q_flag):
        #     if not root:
        #         return False, False, None
        #
        #     if not (p_flag and q_flag):
        #         p1_flag, q1_flag, node1 = getTheNode(root.left, p, q, False, False)
        #         p2_flag, q2_flag, node2 = getTheNode(root.right, p, q, False, False)
        #         p_flag = root == p
        #         q_flag = root == q
        #
        #     p_flag = p_flag or p1_flag or p2_flag
        #     q_flag = q_flag or q1_flag or q2_flag
        #     node = node1 if node2 is None else node2
        #     if p_flag and q_flag:
        #         node = root if node is None else node
        #     return p_flag, q_flag, node
        #
        # p_flag, q_flag, node = getTheNode(root, p, q, False, False)
        # return node
        def getTheNode(root):
            if not root:
                return False

            left = getTheNode(root.left)
            right = getTheNode(root.right)
            mid = root == p or root == q
            if mid + left + right >= 2:
                self.theNode = root

            return left or right or mid

        self.theNode = None
        getTheNode(root)
        return self.theNode


s = Solution()
dp = getTree([0, 1, 2, 3, 4, 5, 6])
assert s.lowestCommonAncestor(dp[0], dp[5], dp[6]) == dp[2]

dp = getTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
assert s.lowestCommonAncestor(dp[0], dp[1], dp[2]) == dp[0]

dp = getTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
assert s.lowestCommonAncestor(dp[0], dp[1], dp[10]) == dp[1]

dp = getTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
assert s.lowestCommonAncestor(dp[0], dp[0], dp[1]) == dp[0]
