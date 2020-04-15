# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2:
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def generateList(lLeft):
    if lLeft:
        return ListNode(lLeft[0], generateList(lLeft[1:]))


def showList(l: ListNode):
    while l:
        print(l.val)
        l = l.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # if not head:
        #     return None
        # dp = [head]
        # currentNode = head.next
        # dp[0].next = None
        # while currentNode:
        #     for i in range(len(dp) - 1, -1, -1):
        #         if dp[i].val <= currentNode.val:
        #             dp.insert(i + 1, currentNode)
        #             currentNode = currentNode.next
        #             dp[i].next = dp[i + 1]
        #             dp[i + 1].next = dp[i + 2] if i + 2 < len(dp) else None
        #             break
        #         elif i == 0:
        #             dp.insert(0, currentNode)
        #             currentNode = currentNode.next
        #             dp[0].next = dp[1]
        # return dp[0]
        def sort(head):
            if head.next is None:
                return head, None
            l1, l2 = sort(head)
            return mergeList(l1, l2)

        def mergeList(l1, l2):
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            if l1.val < l2.val:
                l2.next = mergeList(l1, l2.next)
                return l2
            else:
                l1.next = mergeList(l1.next, l2)
                return l1

        return mergeList(sort(head))


s = Solution()
l1 = generateList([5, 4, 3, 2, 1])
l2 = s.sortList(l1)
showList(l2)

l1 = generateList([1, 2, 3, 4, 5])
l2 = s.sortList(l1)
showList(l2)

l1 = generateList([1, 1, 1, 1])
l2 = s.sortList(l1)
showList(l2)

l1 = generateList([])
l2 = s.sortList(l1)
showList(l2)

l1 = generateList([234, 4, 534, 2, 343, 25, 43, 5, 436, 54, 6, 547, 657, 567, 2, 34, 23, 4, 345, 34, 52, 34, 435])
l2 = s.sortList(l1)
showList(l2)
