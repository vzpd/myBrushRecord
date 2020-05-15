# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例:
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Definition for a binary tree node.node

from collections import deque, OrderedDict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


def createTree(nums: List, i=0):
    if i < len(nums) and nums[i]:
        root = TreeNode(nums[i])
        root.left = createTree(nums, i * 2 + 1)
        root.right = createTree(nums, i * 2 + 2)
        return root


class Solution:
    # def rightSideView(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     dp = [[root]]
    #     res = [root.val]
    #     while 1:
    #         temp = []
    #         for x in dp[-1]:
    #             if x.left:
    #                 temp.append(x.left)
    #             if x.right:
    #                 temp.append(x.right)
    #         if temp:
    #             res.append(temp[-1].val)
    #             dp.append(temp)
    #         else:
    #             break
    #
    #     return res

    # 使用deque实现
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue = deque([(root, 0)])
        dict = OrderedDict()
        while queue:
            node, depth = queue.popleft()
            if node:
                dict[depth] = node.val
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        return [dict.get(x) for x in dict.keys()]


s = Solution()
root = createTree([1, 2, 3, None, 5, None, 4])
assert s.rightSideView(root) == [1, 3, 4]
assert s.rightSideView(None) == []
root = createTree([1, 2, 3, 4, 5, None, None, 6])
assert s.rightSideView(root) == [1, 3, 5, 6]
