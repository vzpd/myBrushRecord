# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        temp = [root]
        res = []
        while temp:
            if temp[-1].left is not None:
                temp.append(temp[-1].left)
                temp[-2].left = None
            else:
                node = temp.pop(-1)
                res.append(node.val)
                if node.right:
                    temp.append(node.right)

        return res


s = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t2.left = t3
assert s.inorderTraversal(t1) == [1, 3, 2]
t1 = TreeNode(1)
assert s.inorderTraversal(t1) == [1]
