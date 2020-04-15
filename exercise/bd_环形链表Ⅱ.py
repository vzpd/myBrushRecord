# Definition for singly-linked list.
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
    def detectCycle(self, head: ListNode) -> ListNode:
        # 方法一：每次经过节点放到set列，如果遇到断点，则退出，返回空，
        # 如果节点在set中存在，则返回此节点
        # dp = set()
        # while head:
        #     if head in dp:
        #         return head
        #     else:
        #         dp.add(head)
        #     head = head.next
        # return None
        # 方法二：双指针法
        # a...Ⅰ....b...Ⅱ...c...Ⅲ...d
        #          .                 .
        #          ...................
        # a节点到b节点，b到c，c到d,中间的距离分别为Ⅰ、Ⅱ、Ⅲ
        # 这些节点中间都存在若干节点，
        # 最后d节点指向b节点，b-c-d形成环
        # 第一阶段：
        # slow每次走一个节点，fast每次走2个基点
        # fast比slow快，如果存在环，最终fast会在第二圈的是与slow会相遇，假设最后在c节点相遇
        # 第二阶段：
        # 由于fast的速度是slow的2倍
        # 因此有如下公式
        # distance(fast)=2*distance(slow)
        # Ⅰ+Ⅱ+Ⅲ+Ⅱ=2*（Ⅰ+Ⅱ）
        # Ⅰ+2*Ⅱ+Ⅲ=2*Ⅰ+2*Ⅱ
        # Ⅰ+Ⅲ=2*Ⅰ
        # Ⅰ=Ⅲ
        # 根据如上公式可以得出Ⅰ和Ⅲ相等
        # 因此如果fast从a节点开始走，show从c节点开始走，fast和slow每次都只走一步
        # 由于Ⅰ和Ⅲ的距离相等，因此他们最终会在b节点相遇
        # 算法如下：
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None


s = Solution()
l = generateList([1, 2, 3, 4, 5, 6])
assert s.detectCycle(l) == None
print(0)

l = generateList([1, 2, 3])
l.next.next.next = l
assert s.detectCycle(l) == l
print(1)
l = generateList([1, 2, 3])
l.next.next.next = l.next
assert s.detectCycle(l) == l.next
print(2)
l = generateList([1, 2, 3])
l.next.next.next = l.next.next
assert s.detectCycle(l) == l.next.next
print(3)
l = generateList([1])
assert s.detectCycle(l) == None
