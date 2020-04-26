import time
from typing import List


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = time.time()  # 程序开始时间
        res = func(*args, **kwargs)
        over_time = time.time()  # 程序结束时间
        total_time = (over_time - start_time) * 1000
        if total_time > 0.1:
            print('程序%s运行用时%s毫秒' % (func.__name__, round(total_time, 3)))
        else:
            print('程序%s运行用时%s微秒' % (func.__name__, round(total_time * 1000, 3)))
        return res

    return int_time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list2ListNode(nums: List) -> ListNode:
    if nums:
        currNode = ListNode(nums[0])
        currNode.next = list2ListNode(nums[1:])
        return currNode


def listNode2List(root: ListNode) -> List:
    res = []
    while root:
        res.append(root.val)
        root = root.next
    return res
