class link:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.maxCount = capacity
        self.head = link(-1)
        self.tail = link(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.dict = {}
        self.linkDict = {}
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.dict:
            value = self.dict[key]
            if self.linkDict[key].next != self.tail:
                self.popNode(key)
                self.addNode(key, value)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            if self.linkDict[key].next != self.tail:
                self.popNode(key)
                self.addNode(key, value)
        else:
            self.count += 1
            self.dict[key] = value

            self.addNode(key, value)
            if self.count > self.maxCount:
                self.popNode()

    def popNode(self, key=None):
        if key is None:
            curr = self.head.next
        else:
            curr = self.linkDict[key]
        curr.next.pre = curr.pre
        curr.pre.next = curr.next
        self.dict.pop(curr.val)
        self.linkDict.pop(curr.val)

    def addNode(self, key, value):
        curr = link(key)
        curr.pre = self.tail.pre
        curr.pre.next = curr
        curr.next = self.tail
        self.tail.pre = curr
        self.dict[key] = value
        self.linkDict[key] = curr


from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(False)


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1  # 返回  1
cache.put(3, 3)  # 该操作会使得密钥 2 作废
assert cache.get(2) == -1  # 返回 -1 (未找到)
cache.put(4, 4)  # 该操作会使得密钥 1 作废
assert cache.get(1) == -1  # 返回 -1 (未找到)
assert cache.get(3) == 3  # 返回  3
assert cache.get(4) == 4  # 返回  4

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4

cache = LRUCache(1)
cache.put(2, 1)
assert cache.get(2) == 1
cache.put(3, 2)
assert cache.get(2) == -1
assert cache.get(3) == 2

cache = LRUCache(2)
cache.put(2, 1)
cache.put(2, 2)
cache.get(2)
cache.put(1, 1)
cache.put(4, 1)
cache.get(2)

cache = LRUCache(2)
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
assert cache.get(1) == -1
assert cache.get(2) == 3

cache = LRUCache(2)
cache.put(2, 1)
cache.put(3, 2)
cache.get(3)
cache.get(2)
cache.put(4, 3)
cache.get(2)
cache.get(3)
cache.get(4)

cache = LRUCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.put(4, 4)
assert cache.get(4) == 4
assert cache.get(3) == 3
assert cache.get(2) == 2
assert cache.get(1) == -1
cache.put(5, 5)
assert cache.get(1) == -1
assert cache.get(2) == 2
assert cache.get(3) == 3
assert cache.get(4) == -1
assert cache.get(5) == 5
