# 我们从二叉树的根节点 root 开始进行深度优先搜索。
#
# 在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
#
# 如果节点只有一个子节点，那么保证该子节点为左子节点。
#
# 给出遍历输出 S，还原树并返回其根节点 root。
#
#  
#
# 示例 1：
#
#
#
# 输入："1-2--3--4-5--6--7"
# 输出：[1,2,5,3,4,6,7]
# 示例 2：
#
#
#
# 输入："1-2--3---4-5--6---7"
# 输出：[1,2,5,3,null,6,null,4,null,7]
# 示例 3：
#
#
#
# 输入："1-401--349---90--88"
# 输出：[1,401,null,349,88,90]
#  
#
# 提示：
#
# 原始树中的节点数介于 1 和 1000 之间。
# 每个节点的值介于 1 和 10 ^ 9 之间。
# Definition for a binary tree node.

from exercise.myUtils import timer


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @timer
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # def getnum(s):
        #     if not s:
        #         return None
        #     num = ''
        #     while s and s[0] != '-':
        #         num += s[0]
        #         s = s[1:]
        #     return num
        #
        # def getlr(s):
        #     if not s:
        #         return None, None
        #     level = ''
        #     while s and s[0] == '-':
        #         level += '-'
        #         s = s[1:]
        #
        #     templevel = ''
        #     index = 0
        #     while index < len(s):
        #         if s[index] == '-':
        #             templevel += '-'
        #         elif templevel == level:
        #             break
        #         else:
        #             templevel = ''
        #         index += 1
        #
        #     num = getnum(s)
        #     lnode = TreeNode(int(num))
        #     if index == len(s):
        #         lnode.left, lnode.right = getlr(s[len(num):])
        #     else:
        #         lnode.left, lnode.right = getlr(s[len(num):index - len(level)])
        #     num = getnum(s[index:])
        #     rnode = None
        #     if num:
        #         rnode = TreeNode(int(num))
        #         rnode.left, rnode.right = getlr(s[index + len(num):])
        #
        #     return lnode, rnode
        #
        # num = getnum(S)
        # root = TreeNode(int(num))
        # root.left, root.right = getlr(S[len(num):])
        # return root
        S += '-'
        q = [TreeNode(-1)]
        level = 0
        num = ''
        for i in range(len(S)):
            if S[i] == '-':
                if S[i - 1] != '-':
                    node = TreeNode(int(num))
                    if level > len(q) - 2:
                        q[-1].left = node
                    else:
                        while len(q)-1 > level :
                            q.pop()
                        q[-1].right = node
                    q.append(node)
                    level = 0
                    num = ''
                level += 1
            else:
                num += S[i]
        return q[0].left


s = Solution()
root = s.recoverFromPreorder('1-2--3---4-5--6---7')
root = s.recoverFromPreorder('1-401--349---90--88---888')
root = s.recoverFromPreorder('1-2--3--4-5--6--7')
root = s.recoverFromPreorder('1-1')
root = s.recoverFromPreorder('1')
root = s.recoverFromPreorder('10-4-2--9---6----6-----9--5')
a = 1
